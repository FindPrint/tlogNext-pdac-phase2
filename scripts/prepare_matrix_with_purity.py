#!/usr/bin/env python3
"""Joint pureté InfiniumPurify à la matrice enrichie.

Usage:
  python scripts/restore_tcga_enriched_p2.py
  # placer purity_infiniumpurify_paad.txt (Zenodo 253193) dans data/
  python scripts/prepare_matrix_with_purity.py

Sortie: data/tcga_enriched_p2_with_purity.csv
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
MAT = ROOT / "data" / "tcga_enriched_p2.csv"
PUR = ROOT / "data" / "purity_infiniumpurify_paad.txt"
OUT = ROOT / "data" / "tcga_enriched_p2_with_purity.csv"

def main():
    if not MAT.exists():
        raise SystemExit(f"Missing {MAT} — run restore_tcga_enriched_p2.py first")
    mat = pd.read_csv(MAT)
    if not PUR.exists():
        raise SystemExit(
            f"Missing {PUR}\n"
            "Download PAAD.txt from Zenodo 253193 (TCGA_tumor_purity.zip) "
            "and save as data/purity_infiniumpurify_paad.txt"
        )
    pur = pd.read_csv(PUR, sep="\t")
    pur["sample15"] = pur["SampleName"].astype(str).str.slice(0, 15)
    merged = mat.merge(
        pur[["sample15", "Purity_InfiniumPurify"]],
        on="sample15",
        how="left",
    )
    OUT.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(OUT, index=False)
    n = merged["Purity_InfiniumPurify"].notna().sum()
    print(f"OK {OUT}  n={len(merged)}  with_purity={n}")

if __name__ == "__main__":
    main()
