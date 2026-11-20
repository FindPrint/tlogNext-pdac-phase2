# SAFE MODE v6.2.1-safe — implémenté

Version pipeline : `v6.2.1-safe-L7aL7b-CohenD-short`

## Utilisation

```bash
python scripts/universal_v6.2.0_cohen.py \
  --input data/pdac_v6_input.csv \
  --control kras_rank --target cea_resid_purity \
  --mode fast --domain biology \
  --output pipeline_runs/v6_full_pdac \
  --seed 42 --no-dashboard --no-telemetry

# Après interruption :
python scripts/universal_v6.2.0_cohen.py ... --output pipeline_runs/v6_full_pdac --resume
```

## Ce qui a été ajouté dans le .py

1. **Helpers** `save_ckpt` / `load_ckpt` / `ckpt_done` (JSON sous `{output}/checkpoints/`)
2. **CLI** `--resume`
3. **Checkpoint `01_mc_opt`** après optimisation Monte Carlo
4. **Checkpoint `02_t0`** après détection T0
5. **Checkpoint `03_landscape`** après figures paysage / tension
6. **Skip MC** si `--resume` et `01_mc_opt.json` présent avec `best_config`

## Test smoke (PDAC)

```
[SAFE] checkpoint OK -> .../01_mc_opt.json
[T0-VALEUR-BRUTE] T0=44.61% -> kras_rank≈79
[SAFE] checkpoint OK -> .../02_t0.json
```

## Limites actuelles

- Le resume **saute le MC** (gros gain), mais ne rejoue pas encore depuis le paysage sans recalcul amont des estimateurs.
- Les horizons L* n’ont pas encore de checkpoints individuels (prochaine itération).
- Fichier local : `scripts/universal_v6.2.0_cohen.py` (~627 ko) — trop volumineux pour un seul commit API ici ; le code patché est sur la machine de travail.

## Prototype séparé (inchangé)

`scripts/run_v6_safe.py` reste le runner léger PDAC Q4 entièrement checkpointé.
