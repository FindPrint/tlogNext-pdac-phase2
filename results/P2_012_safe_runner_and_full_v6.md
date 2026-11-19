# P2.12 — Runner safe (checkpoints disque) + note pipeline full v6.2

## Problème d’environnement

Dans un environnement qui peut timeout / redémarrer, un pipeline long sans checkpoints perd tout le travail. Solution : **écrire chaque étape majeure sur disque** et permettre `--resume`.

## Ce qui a été livré

### `scripts/run_v6_safe.py`
Runner ciblé PDAC (axe kras_high → cea_resid_purity) avec :

| Stage | Contenu |
|-------|--------|
| 00_validate_input | n, colonnes, SHA256 input |
| 01_descriptive | Spearman + Cohen-d kras_high |
| 02_null_permutations | 2000 nuls, null_p |
| 03_cohen_effect | verdict retained / drop |
| 04_residual_checks | contrôle négatif mtap_del |
| 05_export_summary | SUMMARY.json + SUMMARY.md |

**Reprise :**
```bash
python scripts/run_v6_safe.py --input data/pdac_v6_input.csv \\
  --control kras_rank --target cea_resid_purity \\
  --outdir pipeline_runs/pdac_kras_cea --resume
```

### Résultat du run (seed=42, 2000 nuls)
- Cohen d = **+0,344**
- null_p = **0,047** → **retained = True**
- Contrôle négatif mtap_del : null_p = 0,243 (pass)

Cohérent avec P2.9 (légère variation de seed / implémentation).

## Pipeline full UNIVERSAL_LOG v6.2

Le fichier complet (`universal_v6.2.0_cohen.py`, ~13k lignes) est **conçu pour des séries temporelles multi-flux** (complexité, cascades L1–L7, MC harmonique). Il n’est **pas** un test case-control binaire.

Pour l’utiliser « full » sur PDAC il faudrait :
1. Mapper `kras_rank` → control_col
2. Mapper `cea_resid_purity` (+ autres) → flux
3. Accepter que les sorties (seuils, L7, etc.) soient interprétées dans ce cadre

### Recommandation « mode safe » pour le vrai v6

Ajouter dans le full pipeline :

1. **Stage registry** (liste ordonnée d’étapes nommées)
2. **Checkpoint JSON** après chaque étape lourde (scan, bootstrap, nulls, L7…)
3. **CLI** `--resume` + `--outdir`
4. **Idempotence** : chaque étape lit ses inputs depuis disque / checkpoints précédents
5. **Journal** `journal.jsonl` pour audit

Le fichier `run_v6_safe.py` est un **prototype minimal** de ce design, applicable à l’axe PDAC retenu. Il peut servir de modèle pour instrumenter le vrai `universal_v6.2.0_cohen.py`.

## Fichiers
- `scripts/run_v6_safe.py` (poussé)
- `data/pdac_v6_input.csv` (locale ; générée depuis matrice + pureté)
- `pipeline_runs/pdac_kras_cea/` (checkpoints + SUMMARY)
- Copie locale du full : `scripts/universal_v6.2.0_cohen.py` (trop gros pour un seul commit API ; déjà dans tes attachments)

*Le full v6 n’a pas été exécuté de bout en bout ici ; le runner safe cible l’axe retenu avec la même discipline de rétention.*
