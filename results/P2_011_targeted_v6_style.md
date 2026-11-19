# P2.11 — Analyse ciblée style UNIVERSAL_LOG (axe retenu)

**Axe unique retenu :** kras_high (quartile supérieur d’expression KRAS) → CEACAM5 (CEA), avec contrôle pureté.

## TCGA-PAAD (n=178 avec pureté)

- Residualisation CEA sur pureté InfiniumPurify
- kras_high = rank KRAS > Q75
- Cohen d (kras_high vs résidu CEA) = **+0,34**
- MW p = 0,033
- null_p (2000 permutations) = **0,054**

→ Frôle le seuil de rétention classique (α=0,05). Effet petit.

## Validation externe (sans pureté individuelle)

| Cohort | n | d | null_p |
|--------|---|---|--------|
| GSE71729 primary | 145 | +0,52 | 0,008 |
| GSE62452 tumor | 69 | +0,68 | 0,019 |

Effets plus forts en externe (données non ajustées pureté).

## Interprétation pour UNIVERSAL_LOG v6.2

Le pipeline full v6.2 (Cohen-d, cascades L1–L7, nuls + rotations) peut être lancé de façon **ciblée** sur :
- Variable d’intérêt : `ceacam5_rank` (ou log2) résidualisé pureté
- Stratification / contraste : `kras_high`
- Covariable : `Purity_InfiniumPurify`
- Contrôles négatifs : mtap_del (doit rester null)

Recommandation : traiter le signal comme **hypothétique faible dans TCGA**, **soutenu par validation externe**. Ne pas le présenter comme robuste sans pureté.

## Fichiers
- `results/P2_009_retention_nulls.md`
- `results/P2_010_GEO_validation.md`
- Matrices GEO dans `data/geo/`

*Prêt pour un run v6.2 full ciblé quand l’environnement le permet.*
