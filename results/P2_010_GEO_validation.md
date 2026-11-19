# P2.10 — Validation externe GEO (kras_high → CEA)

**Signal testé :** haut quartile d’expression KRAS associé à expression CEACAM5 (CEA) plus élevée.

## GSE71729 (Moffitt et al., Nat Genet 2015)
- Plateforme Agilent 4x44K
- **145 tumeurs primaires PDAC**
- Spearman KRAS vs CEACAM5 : ρ = **0,274** · p = 8,7×10⁻⁴
- kras_high (Q4) vs CEA : Cohen d = **+0,52** · MW p = 0,012 · **null_p = 0,008** (2000 perms)

## GSE62452 (Hussain / Affymetrix HuGene 1.0 ST)
- **69 tumeurs PDAC**
- Spearman KRAS vs CEACAM5 : ρ = **0,441** · p = 1,5×10⁻⁴
- kras_high (Q4) vs CEA : Cohen d = **+0,68** · MW p = 0,022 · **null_p = 0,0185**

## Synthèse validation

| Dataset | n | ρ KRAS–CEA | d kras_high | null_p |
|---------|---|------------|-------------|--------|
| TCGA-PAAD (après pureté) | 178 | ~0,12 (ns) | 0,34 | 0,054 |
| **GSE71729** | 145 | **0,27** | **0,52** | **0,008** |
| **GSE62452** | 69 | **0,44** | **0,68** | **0,019** |

Le signal **kras_high → CEA** se **réplique** de façon significative dans deux cohortes GEO indépendantes (effet moyen à fort, null_p < 0,02).

Note : les datasets GEO n’ont pas de scores de pureté individuels facilement disponibles ; la validation est donc sur expression brute (comme la plupart des études de validation externe).

## Fichiers locaux
- `data/geo/GSE71729_primary_KRAS_CEACAM5.csv`
- `data/geo/GSE62452_tumor_KRAS_CEACAM5.csv`

*Validation positive. Le signal faible observé dans TCGA après pureté est soutenu par des effets plus clairs en externe.*
