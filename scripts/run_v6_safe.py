#!/usr/bin/env python3
"""
Safe / resumable runner for UNIVERSAL_LOG-style analyses in timeout-prone environments.

Design:
- Every major stage writes a JSON checkpoint to disk.
- On restart with --resume, completed stages are skipped.
- Stages are idempotent. Safe against kill/timeout.

Usage:
  python scripts/run_v6_safe.py --input data/pdac_v6_input.csv --mode fast \\
      --control kras_rank --target cea_resid_purity --outdir pipeline_runs/pdac_kras_cea

  # Resume after crash:
  python scripts/run_v6_safe.py ... --resume
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
import traceback
from datetime import datetime, timezone
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats

STAGES = [
    "00_validate_input",
    "01_descriptive",
    "02_null_permutations",
    "03_cohen_effect",
    "04_residual_checks",
    "05_export_summary",
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def stage_path(outdir: Path, stage: str) -> Path:
    return outdir / "checkpoints" / f"{stage}.json"


def stage_done(outdir: Path, stage: str) -> bool:
    p = stage_path(outdir, stage)
    if not p.exists():
        return False
    try:
        return json.loads(p.read_text()).get("status") == "ok"
    except Exception:
        return False


def save_stage(outdir: Path, stage: str, payload: dict) -> None:
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "checkpoints").mkdir(parents=True, exist_ok=True)
    payload = {**payload, "stage": stage, "status": "ok", "finished_at": utc_now()}
    path = stage_path(outdir, stage)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str))
    with open(outdir / "journal.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({"event": "stage_done", "stage": stage, "at": utc_now()}, default=str) + "\n")
    print(f"[SAFE] checkpoint OK → {path}")


def load_stage(outdir: Path, stage: str) -> dict:
    return json.loads(stage_path(outdir, stage).read_text())


def stage_00_validate_input(df, args, outdir):
    required = [args.control, args.target]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing columns: {missing}")
    n = len(df)
    if n < 30:
        raise SystemExit(f"Too few rows: {n}")
    info = {
        "n": n,
        "columns": list(df.columns),
        "control": args.control,
        "target": args.target,
        "input_sha256": sha256_file(Path(args.input)),
    }
    save_stage(outdir, "00_validate_input", info)
    return info


def stage_01_descriptive(df, args, outdir):
    ctrl = df[args.control].values
    tgt = df[args.target].values
    r, p = stats.spearmanr(ctrl, tgt)
    high = ctrl > np.quantile(ctrl, 0.75)
    g0, g1 = tgt[~high], tgt[high]
    if len(g0) >= 5 and len(g1) >= 5:
        u, p_mw = stats.mannwhitneyu(g0, g1, alternative="two-sided")
        d = float((g1.mean() - g0.mean()) / np.sqrt((g0.var() + g1.var()) / 2 + 1e-12))
    else:
        p_mw, d = None, None
    payload = {
        "spearman_rho": float(r),
        "spearman_p": float(p),
        "kras_high_style": {
            "n_high": int(high.sum()),
            "cohen_d": d,
            "mw_p": float(p_mw) if p_mw is not None else None,
        },
    }
    save_stage(outdir, "01_descriptive", payload)
    return payload


def stage_02_null_permutations(df, args, outdir):
    rng = np.random.default_rng(args.seed)
    ctrl = df[args.control].values.copy()
    tgt = df[args.target].values.copy()
    high = ctrl > np.quantile(ctrl, 0.75)
    obs_d = float((tgt[high].mean() - tgt[~high].mean()) / np.sqrt((tgt[high].var() + tgt[~high].var()) / 2 + 1e-12))
    null_ds = []
    for _ in range(args.n_null):
        lab = rng.permutation(high)
        d = (tgt[lab].mean() - tgt[~lab].mean()) / np.sqrt((tgt[lab].var() + tgt[~lab].var()) / 2 + 1e-12)
        null_ds.append(float(d))
    null_ds = np.asarray(null_ds)
    null_p = float((np.abs(null_ds) >= abs(obs_d)).mean())
    payload = {
        "obs_cohen_d": obs_d,
        "null_p": null_p,
        "n_null": args.n_null,
        "null_mean": float(null_ds.mean()),
        "null_std": float(null_ds.std()),
        "seed": args.seed,
    }
    pd.Series(null_ds).to_csv(outdir / "null_cohen_d_distribution.csv", index=False, header=["cohen_d"])
    save_stage(outdir, "02_null_permutations", payload)
    return payload


def stage_03_cohen_effect(df, args, outdir):
    desc = load_stage(outdir, "01_descriptive")
    nulls = load_stage(outdir, "02_null_permutations")
    retained = (nulls["null_p"] < 0.05) and (desc["kras_high_style"]["cohen_d"] is not None)
    payload = {
        "cohen_d": desc["kras_high_style"]["cohen_d"],
        "mw_p": desc["kras_high_style"]["mw_p"],
        "null_p": nulls["null_p"],
        "retained": bool(retained),
        "rule": "null_p < 0.05",
    }
    save_stage(outdir, "03_cohen_effect", payload)
    return payload


def stage_04_residual_checks(df, args, outdir):
    out = {}
    if "mtap_del" in df.columns:
        g = df["mtap_del"].astype(bool).values
        v = df[args.target].values
        if g.sum() >= 5 and (~g).sum() >= 5:
            d = float((v[g].mean() - v[~g].mean()) / np.sqrt((v[g].var() + v[~g].var()) / 2 + 1e-12))
            rng = np.random.default_rng(args.seed + 1)
            null_ds = []
            for _ in range(min(1000, args.n_null)):
                lab = rng.permutation(g)
                dd = (v[lab].mean() - v[~lab].mean()) / np.sqrt((v[lab].var() + v[~lab].var()) / 2 + 1e-12)
                null_ds.append(dd)
            null_p = float((np.abs(null_ds) >= abs(d)).mean())
            out["mtap_del_neg_control"] = {"cohen_d": d, "null_p": null_p, "pass": null_p > 0.05}
    save_stage(outdir, "04_residual_checks", out)
    return out


def stage_05_export_summary(df, args, outdir):
    pieces = {}
    for st in STAGES[:-1]:
        if stage_done(outdir, st):
            pieces[st] = load_stage(outdir, st)
    summary = {
        "pipeline": "run_v6_safe (PDAC targeted, checkpointed)",
        "input": args.input,
        "control": args.control,
        "target": args.target,
        "mode": args.mode,
        "stages": pieces,
        "final_verdict": pieces.get("03_cohen_effect", {}),
        "generated_at": utc_now(),
    }
    (outdir / "SUMMARY.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
    lines = [
        "# UNIVERSAL_LOG-style safe run — summary",
        f"- input: `{args.input}`",
        f"- control: `{args.control}` · target: `{args.target}`",
        f"- n nulls: {args.n_null} · seed: {args.seed}",
        "",
        "## Verdict",
        f"- Cohen d = {summary.get('final_verdict', {}).get('cohen_d')}",
        f"- null_p = {summary.get('final_verdict', {}).get('null_p')}",
        f"- retained = {summary.get('final_verdict', {}).get('retained')}",
    ]
    if "04_residual_checks" in pieces:
        nc = pieces["04_residual_checks"].get("mtap_del_neg_control", {})
        lines.append(f"- neg control mtap_del null_p = {nc.get('null_p')} (pass={nc.get('pass')})")
    (outdir / "SUMMARY.md").write_text("\n".join(lines) + "\n")
    save_stage(outdir, "05_export_summary", {"summary_path": str(outdir / "SUMMARY.json")})
    return summary


STAGE_FUNCS = {
    "00_validate_input": stage_00_validate_input,
    "01_descriptive": stage_01_descriptive,
    "02_null_permutations": stage_02_null_permutations,
    "03_cohen_effect": stage_03_cohen_effect,
    "04_residual_checks": stage_04_residual_checks,
    "05_export_summary": stage_05_export_summary,
}


def main():
    ap = argparse.ArgumentParser(description="Safe resumable runner for PDAC kras_high→CEA axis")
    ap.add_argument("--input", required=True)
    ap.add_argument("--control", default="kras_rank")
    ap.add_argument("--target", default="cea_resid_purity")
    ap.add_argument("--mode", default="fast", choices=["fast", "robust", "full"])
    ap.add_argument("--outdir", default="pipeline_runs/pdac_kras_cea")
    ap.add_argument("--n-null", type=int, default=2000)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--resume", action="store_true")
    args = ap.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)
    (outdir / "checkpoints").mkdir(parents=True, exist_ok=True)

    meta = {"started_at": utc_now(), "argv": sys.argv, "input": args.input, "resume": args.resume}
    (outdir / "run_meta.json").write_text(json.dumps(meta, indent=2))

    df = pd.read_csv(args.input)
    print(f"[SAFE] loaded {args.input} shape={df.shape}")
    print(f"[SAFE] outdir={outdir} resume={args.resume}")

    for stage in STAGES:
        if args.resume and stage_done(outdir, stage):
            print(f"[SAFE] skip {stage} (already done)")
            continue
        print(f"[SAFE] running {stage} ...")
        t0 = time.time()
        try:
            STAGE_FUNCS[stage](df, args, outdir)
            print(f"[SAFE] {stage} done in {time.time()-t0:.1f}s")
        except Exception as e:
            err = {"status": "error", "stage": stage, "error": str(e), "traceback": traceback.format_exc(), "at": utc_now()}
            stage_path(outdir, stage).write_text(json.dumps(err, indent=2))
            print(f"[SAFE] FAILED at {stage}: {e}")
            sys.exit(1)

    print(f"[SAFE] all stages complete → {outdir / 'SUMMARY.md'}")


if __name__ == "__main__":
    main()
