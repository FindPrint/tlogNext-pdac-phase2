# P2.7 — KRAS → CEA / CA125 après contrôle pureté

**n = 178** (InfiniumPurify matchés)

## Spearman

| Axis | Modèle | ρ | p |
|------|--------|---|---|
| CEA | brut | 0,343 | 2,7×10⁻⁶ |
| CEA | target ~ pureté puis ~ ~ KRAS | 0,138 | **0,067** |
| CEA | les deux résidualisés | 0,116 | 0,122 |
| CA125 | brut | 0,278 | 1,7×10⁻⁴ |
| CA125 | target ~ pureté puis ~ KRAS | 0,166 | **0,027** |
| CA125 | les deux résidualisés | 0,143 | 0,057 |

## kras_high (quartile supérieur) vs CEA résidualisé pureté

- MW p = **0,033**
- médiane résidu low ≈ −4,6 · high ≈ +18
- Cohen d ≈ 0,34

## Verdict

- Le signal **KRAS ↔ CEA** est **fortement atténué** par la pureté (passe de p≈3×10⁻⁶ à p≈0,07–0,12).
- Un effet résiduel du **haut quartile KRAS** sur CEA après pureté reste détectable (p=0,033, d≈0,34).
- CA125 se comporte de façon similaire (légèrement plus résistant).
- Conclusion provisoire : une partie du signal KRAS→sécrétoire est indépendante de la pureté, mais l’effet global est beaucoup plus faible qu’annoncé sans contrôle pureté.

## Fichiers
- `results/p2_007_kras_purity_control.csv`
- Source pureté : Zenodo 253193 (InfiniumPurify)

*Négatif partiel honnête. Priorité suivante : UNIVERSAL_LOG v6.2 avec pureté covariable.*
