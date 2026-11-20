# P2.16 — Run full UNIVERSAL_LOG v6.2.1-safe **terminé**

**Sortie :** `pipeline_runs/v6_safe_test/`  
**Commande :** mode `fast`, control=`kras_rank`, target=`cea_resid_purity`, domain=`biology`, seed=42

```
✓ Pipeline Master completed successfully!
```

## Cascades de seuils

| Seuil | % progression | kras_rank brut |
|-------|---------------|----------------|
| T-2 | 0,0 % | ~1 |
| T-1 | 25,5 % | ~46 |
| **T0** | **44,6 %** | **~79** |
| T+1 / T+2 | 77,3 % | ~138 |

## L1–L7 (synthèse)

| Niveau | Verdict |
|--------|--------|
| **L1 cible (CEA resid)** | direction **down** · conf ~0,57 · relative_change ≈ −0,47 |
| **L3 régime** | **post** T0 · crossing_prob 0,90 · conf ~0,82 |
| **L4 risque** | **high** · risk_score ≈ 0,72 |
| **L5 complexité** | ranking estimateurs OK |
| **L7a cohérence** | vote **UP** (22 %) mais **disagreement** cible=down / régime=up |
| **L7b robustesse** | **FRAGILE** (mode light) |

### Checks L7b light
- stabilité horizon : **PASS**
- stabilité walk-forward T0 : **FAIL** (t0_std ≈ 24 > 20)
- cohérence interne L1 vs L3 : **FAIL** (sens opposés)

## Tension holographique
- Régime : **divergence** | control=kras_rank
- Δ = **3,86** · D_vec ≈ [1,58 · 3,31 · 5,44 · 2,49]

## Walk-forward adaptatif
- n_folds=5 · window=89 · dir_acc=80 %
- **t0_stable=False** (T0 instable entre folds)

## Lecture intégrée (biologie PDAC)

1. Le full v6 **confirme** un paysage en **divergence** le long de kras_rank, T0≈79.
2. L1 sur **cea_resid_purity** dit **down** après le seuil ; L3 dit **post-régime** — d’où le désaccord L7a/L7b.
3. L7b **FRAGILE** : ne pas traiter le consensus directionnel comme robuste.
4. Le signal biologique prioritaire reste l’effet **Q4 kras_high → CEA** (tests de rétention + GEO), **pas** le T0 continuum comme biomarqueur CEA.
5. T0 variable en walk-forward → le seuil de complexité n’est pas stable au sous-échantillonnage.

## Fichiers clés produits
- `master_results.json` (~7 Mo)
- `universal_master_report.txt`
- `reading_synthesis.json`
- `df_feat.csv`, `scores.json`, `transition_analysis.json`
- PNG : landscape, holographic_tension, separation_*, threshold_scan, …
- checkpoints : `01_mc_opt`, `02_t0`, `03_landscape`

## Suite éventuelle
- `--l7b-full` pour audit graine/fenêtre/mélange (×3–4 temps)
- Contraste binaire `kras_high` comme control (mieux aligné sur le signal Q4)
- Jointure ESTIMATE/CPE pureté
