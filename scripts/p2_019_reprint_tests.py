"""Reprint P2.19 tests from data/joined_kras_allele_survival.csv."""
import pandas as pd
import numpy as np
from scipy import stats
from pathlib import Path
from lifelines.statistics import logrank_test
from lifelines import CoxPHFitter

p = Path(__file__).resolve().parents[1] / "data" / "joined_kras_allele_survival.csv"
m = pd.read_csv(p)
sub = m[m.codon.isin(["G12D", "G12V", "G12R"])]
for col in ["CEACAM5_log2", "KRAS_log2", "classical_proxy", "cea_resid_class"]:
    groups = [sub.loc[sub.codon == c, col].dropna() for c in ["G12D", "G12V", "G12R"]]
    h, pv = stats.kruskal(*groups)
    print(f"KW {col}: H={h:.2f} p={pv:.3g}")
for label, part in {
    "missense": m[m.codon != "no_missense_call"],
    "G12D": m[m.codon == "G12D"],
}.items():
    r, pv = stats.spearmanr(part.KRAS_log2, part.cea_resid_class)
    print(f"{label} rho resid {r:.3f} p={pv:.3g} n={len(part)}")
a = m[m.kras_high == True]
b = m[m.kras_high == False]
res = logrank_test(a.os_months, b.os_months, a.os_event, b.os_event)
print("logrank kras_high", res.p_value)
