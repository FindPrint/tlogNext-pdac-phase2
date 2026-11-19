# P2.13 — Lancement full UNIVERSAL_LOG v6.2.0 sur l’axe PDAC

## Commande utilisée

```bash
MPLBACKEND=Agg PYTHONUNBUFFERED=1 python3 scripts/universal_v6.2.0_cohen.py \
  --input data/pdac_v6_input.csv \
  --control kras_rank \
  --target cea_resid_purity \
  --mode fast \
  --domain biology \
  --output pipeline_runs/v6_full_pdac \
  --seed 42 \
  --no-dashboard \
  --no-telemetry
```

## Ce qui a tourné (partiel — environnement timeout / kill process)

```
UNIVERSAL_LOG v6.2.0-L7aL7b-CohenD-short — RUNNING MASTER PIPELINE
File: data/pdac_v6_input.csv | Domain: biology | Mode: fast
Target: cea_resid_purity | Control: kras_rank

Optimisation Monte Carlo HARMONIQUE GUIDÉ v1 (12 itérations, P=0.45)
✓ Meilleur score: 0.450 | règle: uniform | n_candidates: 93 | w_size: 30 | min_grp: 6

[T0-VALEUR-BRUTE] controle=kras_rank T0=44.61%
  -> valeur brute controle=79 (median_near=79.0, min=77, max=81, spread=4, ambiguous=False)

✓ Paysage des 29 estimateurs sauvegardé: landscape_complexity.png
```

Fichiers produits localement dans `pipeline_runs/v6_full_pdac/` :
- `landscape_complexity.png`
- `landscape_complexity_improved.png`
- `holographic_tension.png`
- `separation_clustermap.png`
- logs partiels `run2.log` / `run3.log`

Le process a été interrompu avant la fin des cascades L1–L7 / export JSON complet (limite d’environnement).

## Interprétation préliminaire T0

Sur la série ordonnée par `kras_rank`, le pipeline place un **T0 à ~44,6 %** de la progression, correspondant à **kras_rank ≈ 79** (autour du milieu–haut de la distribution, cohérent avec la zone Q3/Q4 où l’effet kras_high était observé).

## Nouvelle version livrée pour cet environnement

| Composant | Rôle |
|-----------|------|
| `scripts/run_v6_safe.py` | Runner checkpointé, relançable (`--resume`) |
| `scripts/universal_v6.2.0_cohen.py` | Copie du pipeline full (610 ko) |
| `data/pdac_v6_input.csv` | Entrée ordonnée (kras_rank → cea_resid_purity) |

### Pour finir le run full chez toi

```bash
# depuis le clone du dépôt + matrice restaurée
python scripts/restore_tcga_enriched_p2.py
python scripts/prepare_matrix_with_purity.py   # si pureté présente
# régénérer pdac_v6_input.csv (voir scripts ou notes P2.12)

MPLBACKEND=Agg python3 scripts/universal_v6.2.0_cohen.py \
  --input data/pdac_v6_input.csv \
  --control kras_rank \
  --target cea_resid_purity \
  --mode fast \
  --domain biology \
  --output pipeline_runs/v6_full_pdac \
  --seed 42 \
  --no-dashboard --no-telemetry
```

## Mode safe recommandé pour le full v6

Instrumenter le vrai pipeline avec les mêmes idées que `run_v6_safe.py` :
1. Checkpoint après MC optimization, après paysage estimateurs, après chaque horizon L*
2. `--resume` qui relit les JSON déjà écrits dans `--output`
3. Pas de dépendance à un process long non interrompu

*Run full démarré et partiellement abouti (T0 + landscape). Complétion à faire hors environnement timeout.*
