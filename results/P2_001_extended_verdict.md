# P2 — Analyses étendues MTAP × CA125/CEA (19 nov. 2026)

Matrice : `tcga_enriched_p2.csv` SHA256 `6a53c8c6…`

## Contrôle par KRAS (résidus)

| Cible | Δmédiane résidus | p |
|-------|------------------|---|
| MUC16 | +1,19 | 0,063 (NS strict) |
| CEACAM5 | +1,46 | **0,020** |

→ Le lien MTAP–CEACAM5 **survit** à l’ajustement sur KRAS. MUC16 devient borderline.

## GISTIC ordinal (Spearman)

Plus la délétion est profonde (GISTIC bas), plus MUC16/CEACAM5/KRAS sont élevés :

| Cible | ρ | p |
|-------|---|---|
| MUC16 | −0,25 | **9,5×10⁻⁴** |
| CEACAM5 | −0,33 | **7×10⁻⁶** |
| KRAS | −0,28 | **2×10⁻⁴** |

## Tailles d’effet (Cohen’s d)

| Contraste | MUC16 | CEACAM5 |
|-----------|-------|---------|
| MTAP-del vs intact | +0,35 | +0,52 |
| kras_fort vs reste | +0,61 | +0,69 |

## Stratification kras_fort

- Chez non-fort (n=165) : MTAP→CEACAM5 p=0,004 ; MTAP→MUC16 p=0,057
- Chez kras_fort (n=12) : non significatif (6 vs 6, puissance faible)

## Synthèse

1. Signal **KRAS → CA125/CEA** : solide (inchangé).
2. Signal **MTAP-del → CEACAM5** : résiste à l’ajustement KRAS ; taille d’effet modérée.
3. Signal **MTAP-del → MUC16** : plus fragile après ajustement KRAS.
4. Corrélation ordinale GISTIC cohérente (dose-response).

**Prochaine exigence de rétention :** pureté, nuls permutés, runs v6.2, validation externe.

Pas de claim clinique.
