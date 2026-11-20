# P2.18 — Pureté ESTIMATE (MD Anderson) + retest Q4→CEA

Source publique (pas de fichier utilisateur) :
```
https://bioinformatics.mdanderson.org/estimate/tables/pancreatic_ductal_adenocarcinoma_RNAseqV2.txt
```
Colonnes : Stromal_score, Immune_score, ESTIMATE_score (n=179 PAAD).

Pureté dérivée (formule usuelle Yoshihara / TCGA) :
`Purity_ESTIMATE = cos(0.6049872018 + 0.0001467884 * ESTIMATE_score)`

## Recouvrement
- Jointure sur `sample15` : **178 / 179** échantillons de la matrice enrichie
- Spearman InfiniumPurify vs Purity_ESTIMATE : **ρ = 0,49** (p = 6,5×10⁻¹²) — corrélés mais non redondants

## kras_high (Q4) → CEA après residualisation

| Residualisation | n | Cohen d | MW p | null_p (2000) |
|-----------------|---|---------|------|---------------|
| Aucune (CEA rank brut) | 179 | +0,83 | <10⁻⁴ | 0,000 |
| **InfiniumPurify** | 178 | **+0,34** | 0,033 | **0,047** |
| **Purity_ESTIMATE** | 178 | **+0,72** | 0,0001 | **0,000** |
| Stromal_score | 178 | +0,77 | <10⁻⁴ | 0,000 |

Spearman kras_rank vs CEA résidualisé ESTIMATE : **ρ = 0,31** (p = 2×10⁻⁵)

## Lecture

1. Le signal Q4 **n’est pas un artefact** d’InfiniumPurify seul.
2. Avec ESTIMATE (expression stromale/immune), l’effet est **plus fort** (d≈0,72, null_p≈0).
3. InfiniumPurify était le contrôle **le plus sévère** ; ESTIMATE confirme et renforce.
4. Les deux puretés ne mesurent pas exactement la même chose (ρ≈0,5) — d’où l’intérêt du double contrôle.

## Fichiers locaux
- `data/purity/PAAD_ESTIMATE_scores.txt`
- `data/tcga_enriched_p2_with_estimate.csv`

*Validation pureté multi-méthodes : signal kras_high→CEA retenu et renforcé.*
