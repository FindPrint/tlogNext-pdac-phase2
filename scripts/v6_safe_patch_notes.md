# Patch notes — mode safe pour UNIVERSAL_LOG v6.2.0

Objectif : permettre `--resume` sans perte après timeout/kill.

## Emplacements à instrumenter (fichier ~13k lignes)

1. **Après optimisation MC harmonique**
   - Écrire `checkpoints/01_mc_opt.json` (score, w_size, min_grp, seed, n_candidates)

2. **Après calcul T0 / cascade seuils**
   - `checkpoints/02_t0.json` (T0_pct, valeur brute contrôle, spread)

3. **Après paysage estimateurs** (là où on sauvegarde déjà `landscape_complexity.png`)
   - `checkpoints/03_landscape_done.json` + conserver les PNG

4. **Après chaque horizon / bloc L1–L7**
   - `checkpoints/04_L{h}.json` par horizon

5. **Avant export final JSON**
   - Si tous les checkpoints requis existent et `--resume`, charger et sauter le calcul

## API minimale proposée

```python
from pathlib import Path
import json
from datetime import datetime, timezone

def ckpt_dir(output_dir: str) -> Path:
    p = Path(output_dir) / "checkpoints"
    p.mkdir(parents=True, exist_ok=True)
    return p

def save_ckpt(output_dir, name, payload: dict):
    payload = {**payload, "status": "ok", "finished_at": datetime.now(timezone.utc).isoformat()}
    path = ckpt_dir(output_dir) / f"{name}.json"
    path.write_text(json.dumps(payload, indent=2, default=str))
    return path

def load_ckpt(output_dir, name):
    path = ckpt_dir(output_dir) / f"{name}.json"
    if not path.exists():
        return None
    data = json.loads(path.read_text())
    return data if data.get("status") == "ok" else None
```

## CLI

```text
--resume          # skip stages with OK checkpoints in --output
```

## Comportement

- Sans `--resume` : comportement actuel (réécrit les sorties).
- Avec `--resume` : si `01_mc_opt.json` OK, ne recalcule pas le MC ; idem pour T0 / landscape / L*.
- Toujours écrire les PNG/CSV dès qu’ils sont prêts (déjà le cas pour landscape).

## Priorité d’implémentation

1. Checkpoint après MC + T0 + landscape (couvre 80 % des pertes actuelles)
2. Puis par horizon L*
3. Tests : kill -9 au milieu, relancer avec `--resume`, vérifier identité des sorties numériques (seed fixe)

Prototype de référence déjà validé : `scripts/run_v6_safe.py` (PDAC axe Q4).

*Ne remplace pas le cœur statistique v6.2 ; ajoute uniquement la reprise disque.*
