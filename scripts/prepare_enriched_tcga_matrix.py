#!/usr/bin/env python3
"""
P2 — Préparation de la matrice TCGA enrichie pour les protocoles 001 et 002.

Date : 19 novembre 2026
Objectif : produire un CSV prêt pour UNIVERSAL_LOG v6.2 avec :
  - expression des flux prioritaires (MUC16, CEACAM5, KRAS, panel contexte)
  - VAF KRAS (si disponible dans le MAF)
  - pureté ESTIMATE
  - statut MTAP (GISTIC -2 = délétion profonde)
  - colonnes de contrôle utilisables comme axes

Ce script est conçu pour tourner là où les données brutes sont déjà présentes
(ou téléchargeables). Il ne contient aucune donnée patient.

Entrées attendues (chemins configurables) :
  - Matrice d'expression RSEM normalisée (Firehose PAAD) ou matrice déjà
    construite (ex. celle des flux v4 des archives)
  - mtap_gistic_status.csv (déjà produit dans les archives, SHA b54cb94f…)
  - Fichier de pureté ESTIMATE (TCGA) ou scores déjà calculés
  - MAF ou table de mutations KRAS avec VAF (optionnel mais prioritaire)

Sortie :
  data/tcga_enriched_p2.csv  — une ligne par tumeur, colonnes standardisées
"""

from __future__ import annotations

import argparse
import hashlib
from pathlib import Path
from typing import Optional

import numpy as np
import pandas as pd


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_expression(path: Path, gene_list: list[str]) -> pd.DataFrame:
    """Charge une matrice expression (gènes x échantillons ou inverse) et
    retourne un DataFrame indexé par sample_id avec les gènes demandés.
    """
    df = pd.read_csv(path, sep=None, engine="python", index_col=0)
    # Normaliser : si les gènes sont en colonnes, on transpose
    if any(g in df.columns for g in gene_list):
        expr = df
    elif any(g in df.index for g in gene_list):
        expr = df.T
    else:
        # Essayer de nettoyer les symboles (ex. "MUC16|..." → MUC16)
        df.columns = [str(c).split("|")[0].split("(")[0].strip() for c in df.columns]
        df.index = [str(i).split("|")[0].split("(")[0].strip() for i in df.index]
        if any(g in df.columns for g in gene_list):
            expr = df
        else:
            expr = df.T
    available = [g for g in gene_list if g in expr.columns]
    missing = [g for g in gene_list if g not in expr.columns]
    if missing:
        print(f"[WARN] Gènes absents de la matrice expression : {missing}")
    out = expr[available].copy()
    out.index = out.index.astype(str).str.replace(r"\.\d+$", "", regex=True)  # enlever .01 si besoin
    # Garder uniquement les tumeurs primaires si le barcode le permet
    if out.index.str.contains("-01").any():
        out = out[out.index.str.contains("-01")]
    out.index.name = "sample_id"
    return out


def load_mtap_gistic(path: Path) -> pd.Series:
    """Charge mtap_gistic_status.csv (archives) et retourne une Series
    sample_id → mtap_del (True si GISTIC == -2).
    """
    df = pd.read_csv(path)
    # Chercher la colonne d'identifiant et la colonne GISTIC
    id_col = None
    for c in df.columns:
        if "sample" in c.lower() or "barcode" in c.lower() or "id" in c.lower() or c.lower().startswith("tcga"):
            id_col = c
            break
    if id_col is None:
        id_col = df.columns[0]
    gistic_col = None
    for c in df.columns:
        if "mtap" in c.lower() and ("gistic" in c.lower() or "cn" in c.lower() or "del" in c.lower()):
            gistic_col = c
            break
    if gistic_col is None:
        for c in df.columns:
            if "mtap" in c.lower():
                gistic_col = c
                break
    if gistic_col is None:
        raise ValueError(f"Colonne MTAP/GISTIC introuvable dans {path}. Colonnes : {list(df.columns)}")
    s = df.set_index(id_col)[gistic_col]
    s.index = s.index.astype(str).str.replace(r"\.\d+$", "", regex=True)
    # -2 = délétion profonde
    mtap_del = (s == -2) | (s.astype(str).str.contains("del", case=False, na=False))
    mtap_del.name = "mtap_del"
    return mtap_del.astype(bool)


def load_estimate_purity(path: Path) -> pd.Series:
    """Charge un fichier de pureté ESTIMATE (sample → purity).
    Accepte les formats courants (ESTIMATE score ou pureté dérivée).
    """
    df = pd.read_csv(path, sep=None, engine="python")
    id_col = df.columns[0]
    # Chercher une colonne de pureté
    purity_col = None
    for c in df.columns:
        cl = c.lower()
        if "purity" in cl or "estimate" in cl or "cpe" in cl:
            purity_col = c
            break
    if purity_col is None:
        # Parfois la pureté est 1 - (stromal+immune normalisés)
        if "StromalScore" in df.columns and "ImmuneScore" in df.columns:
            # Approximation simple ; la vraie conversion ESTIMATE→purity
            # utilise une courbe de calibration (Yoshihara / Aran).
            print("[WARN] Conversion Stromal+Immune → pureté non calibrée ; utiliser un fichier pureté pré-calculé si possible.")
            purity_col = None
        else:
            raise ValueError(f"Colonne pureté introuvable dans {path}")
    s = df.set_index(id_col)[purity_col] if purity_col else None
    if s is not None:
        s.index = s.index.astype(str).str.replace(r"\.\d+$", "", regex=True)
        s.name = "purity_estimate"
    return s


def load_kras_vaf(path: Path) -> pd.Series:
    """Charge un MAF ou table de mutations et retourne sample_id → VAF KRAS max.
    Si plusieurs mutations KRAS, on prend la VAF la plus élevée.
    """
    df = pd.read_csv(path, sep=None, engine="python", comment="#")
    # Colonnes typiques MAF
    gene_col = next((c for c in df.columns if c.upper() in ("HUGO_SYMBOL", "GENE", "GENE_SYMBOL")), None)
    sample_col = next((c for c in df.columns if "tumor_sample" in c.lower() or c.lower() in ("sample_id", "barcode", "tumor_sample_barcode")), None)
    vaf_col = next((c for c in df.columns if "vaf" in c.lower() or "allele_frequency" in c.lower() or "t_alt_count" in c.lower()), None)
    if gene_col is None or sample_col is None:
        raise ValueError(f"Colonnes gene/sample introuvables dans {path}")
    kras = df[df[gene_col].astype(str).str.upper() == "KRAS"].copy()
    if vaf_col is None:
        # Essayer de calculer VAF = t_alt / (t_alt + t_ref)
        alt = next((c for c in df.columns if "t_alt" in c.lower()), None)
        ref = next((c for c in df.columns if "t_ref" in c.lower()), None)
        if alt and ref:
            kras["vaf"] = kras[alt] / (kras[alt] + kras[ref]).replace(0, np.nan)
            vaf_col = "vaf"
        else:
            print("[WARN] Pas de VAF ni de counts alt/ref ; VAF non disponible.")
            return pd.Series(dtype=float, name="kras_vaf")
    kras[sample_col] = kras[sample_col].astype(str).str.replace(r"\.\d+$", "", regex=True)
    # Prendre le max VAF par sample
    vaf = kras.groupby(sample_col)[vaf_col].max()
    vaf.name = "kras_vaf"
    return vaf


def main():
    parser = argparse.ArgumentParser(description="Prépare la matrice TCGA enrichie phase 2")
    parser.add_argument("--expression", required=True, help="CSV/TSV matrice expression")
    parser.add_argument("--mtap-gistic", default=None, help="mtap_gistic_status.csv (archives)")
    parser.add_argument("--purity", default=None, help="Fichier pureté ESTIMATE")
    parser.add_argument("--kras-maf", default=None, help="MAF ou table mutations KRAS avec VAF")
    parser.add_argument("--genes", default="MUC16,CEACAM5,KRAS,PGC,CLDN18,REG4,KRT20,DPCR1,CLCA1,MUC2,MUC17,GSTM1",
                        help="Liste de gènes séparés par des virgules")
    parser.add_argument("--output", default="data/tcga_enriched_p2.csv")
    args = parser.parse_args()

    gene_list = [g.strip() for g in args.genes.split(",") if g.strip()]
    print(f"Gènes demandés : {gene_list}")

    expr = load_expression(Path(args.expression), gene_list)
    print(f"Expression chargée : {expr.shape[0]} samples × {expr.shape[1]} gènes")
    print(f"  SHA expression : {sha256_file(Path(args.expression))}")

    out = expr.copy()

    if args.mtap_gistic:
        mtap = load_mtap_gistic(Path(args.mtap_gistic))
        print(f"MTAP GISTIC : {mtap.sum()} délétées / {len(mtap)} | SHA {sha256_file(Path(args.mtap_gistic))}")
        out = out.join(mtap, how="left")
        out["mtap_del"] = out["mtap_del"].fillna(False).astype(bool)

    if args.purity:
        pur = load_estimate_purity(Path(args.purity))
        if pur is not None:
            print(f"Pureté : {pur.notna().sum()} valeurs | SHA {sha256_file(Path(args.purity))}")
            out = out.join(pur, how="left")

    if args.kras_maf:
        vaf = load_kras_vaf(Path(args.kras_maf))
        print(f"KRAS VAF : {vaf.notna().sum()} valeurs | SHA {sha256_file(Path(args.kras_maf))}")
        out = out.join(vaf, how="left")

    # Colonnes de contrôle dérivées
    if "KRAS" in out.columns:
        out["kras_rank"] = out["KRAS"].rank(method="average")
    if "purity_estimate" in out.columns:
        out["purity_rank"] = out["purity_estimate"].rank(method="average")
    if "kras_vaf" in out.columns:
        out["kras_vaf_rank"] = out["kras_vaf"].rank(method="average")
    if "MUC16" in out.columns:
        out["muc16_rank"] = out["MUC16"].rank(method="average")
    if "CEACAM5" in out.columns:
        out["ceacam5_rank"] = out["CEACAM5"].rank(method="average")

    # Ordre stable pour reproductibilité
    out = out.sort_index()
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out.to_csv(out_path)
    print(f"\nMatrice écrite : {out_path} ({out.shape[0]} × {out.shape[1]})")
    print(f"SHA sortie : {sha256_file(out_path)}")
    print("Colonnes :", list(out.columns))
    print("\nPrêt pour P2-PROTO-001 / P2-PROTO-002.")


if __name__ == "__main__":
    main()
