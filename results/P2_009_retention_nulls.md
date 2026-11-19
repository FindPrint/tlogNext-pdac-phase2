# P2.9 — Tests de rétention (nuls) après contrôle pureté

**n = 178** · seed=42 · 2000 permutations  
Axes résidualisés sur pureté InfiniumPurify.

## Résultats (null permutations)

| Test | Stat | null_p | Décision |
|------|------|--------|----------|
| kras_r vs cea_r (continu) | ρ = +0,117 | 0,126 | **DROP** |
| kras_r vs ca125_r | ρ = +0,143 | 0,056 | borderline / DROP |
| **kras_high vs cea_r** | d = +0,344 | **0,054** | **faible RETAIN** |
| kras_high vs ca125_r | d = +0,086 | 0,628 | DROP |
| mtap_del vs cea_r | d = +0,203 | 0,255 | DROP (contrôle négatif OK) |

### Référence sans pureté (pour contraste)
| Test | Stat | null_p |
|------|------|--------|
| kras vs cea RAW | ρ = +0,343 | < 0,001 |
| mtap_del vs cea RAW | d = +0,546 | 0,0015 |

## Verdict de rétention

1. **MTAP → CEA/CA125** : non retenu (confondu pureté + nulls).
2. **KRAS continu → CEA** après pureté : non retenu (null_p > 0,10).
3. **kras_high (Q4) → CEA résidualisé** : seul signal qui frôle le seuil (null_p ≈ 0,054). Effet faible (d ≈ 0,34). À traiter comme **hypothétique / faible**, pas comme signal robuste.

## Critères appliqués (alignés UNIVERSAL_LOG)
- Null permutations (mélange des labels / cibles)
- Residualisation pureté avant test
- Contrôle négatif MTAP (passe correctement)

Rotations circulaires non retenues ici (implémentation à raffiner pour structure d’ordre des ranks).

## Fichiers
- `results/p2_009_retention_nulls_rotations.csv`
- Matrice : `data/tcga_enriched_p2_with_purity.csv` (locale / reconstructible)

*Prochaine étape recommandée : run UNIVERSAL_LOG v6.2 full sur kras_high / cea_r avec pureté, ou validation GEO.*
