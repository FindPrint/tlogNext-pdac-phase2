# P2-PROTO-001 lite — Tests directs (sans pipeline v6.2)

Date : 19 novembre 2026  
Matrice : `tcga_enriched_p2.csv` (SHA256 `6a53c8c6…`, n=179)

## Résultats

| Test | Cible | Stat | p | Interprétation |
|------|-------|------|---|----------------|
| Spearman KRAS vs MUC16 | MUC16 | ρ=0,279 | **1,6e-4** | Association positive confirmée |
| Spearman KRAS vs CEACAM5 | CEACAM5 | ρ=0,342 | **2,8e-6** | Association positive confirmée |
| MW top-quartile KRAS | MUC16 | Δmed=+1,30 | 0,061 | Tendance, NS strict |
| MW top-quartile KRAS | CEACAM5 | Δmed=+2,96 | **1,0e-5** | Fortement plus élevé |
| MW kras_fort (top-12) | MUC16 | Δmed=+1,95 | **0,014** | Confirmé |
| MW kras_fort (top-12) | CEACAM5 | Δmed=+2,59 | **0,006** | Confirmé |
| MW MTAP-del vs intact | MUC16 | Δmed=+1,85 | **0,011** | MUC16 plus haut si MTAP-del |
| MW MTAP-del vs intact | CEACAM5 | Δmed=+1,48 | **0,004** | CEACAM5 plus haut si MTAP-del |
| MW MTAP-del | KRAS | Δmed=+0,08 | 0,14 | Pas de différence KRAS |
| MW MTAP-del | PRMT5 (ARN) | Δmed=+0,06 | 0,88 | Pas de différence expression PRMT5 |
| Fisher kras_fort × MTAP-del | — | OR=3,46 | 0,073 | Même résultat archives (NS) |

## Verdict préliminaire (lite)

1. **Signal CA125/CEA chez KRAS élevé : RETENU au niveau expression** (Spearman + MW top-12 significatifs pour MUC16 et CEACAM5).
2. **Nouveau signal exploratoire :** MTAP-del associé à MUC16 et CEACAM5 plus élevés (p=0,011 et 0,004). À confronter aux nuls / pureté / pipeline v6.2.
3. Expression PRMT5 ne diffère pas selon MTAP (cohérent avec le fait que la dépendance est CRISPR, pas le niveau d’ARN).

## Prochaines étapes

- Ajouter pureté ESTIMATE comme covariable / axe
- Runs v6.2 complets (cascades + nuls + rotations) sur axes kras_rank, muc16_rank, mtap_del
- Validation externe GSE71729 / GSE62452 si matrices disponibles

**Ce n’est pas un verdict clinique.** Critères de rétention stricts (nul + rotation + orthogonalité) pas encore appliqués via le pipeline.
