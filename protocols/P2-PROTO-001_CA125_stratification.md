# P2-PROTO-001 — Stratification CA125 (MUC16) / CEA chez KRAS élevé

**Statut :** gelé le 19 novembre 2026  
**Priorité :** 1 (signal le plus robuste du projet)  
**Instrument :** UNIVERSAL_LOG v6.2 (Cohen-d, SHA `f07567c4…ec3abf` — archives)

---

## Question

Le signal d’expression « groupe KRAS le plus élevé → CA125 et CEA élevés » (confirmé 3/4 cohortes) + le lien de survie de CA125 (2/3 cohortes) peut-il être raffiné en un biomarqueur de stratification utilisable, en testant des axes plus légitimes que le simple rang KRAS et en exigeant les critères de rétention stricts (nul + rotation + orthogonalité) ?

## Données

- **Primaire :** TCGA-PAAD Firehose / matrices déjà construites (178 tumeurs primaires), enrichies si possible de :
  - VAF KRAS (depuis MAF)
  - Pureté ESTIMATE
  - Statut MTAP (deep deletion 9p21)
- **Validation externe :** GSE71729 (145), GSE62452 (69), ICGC (si expression CA125 disponible)
- **Orthogonalité :** CPTAC (protéine MUC16/CEACAM5 si mesurée), survie TCGA/ICGC, pureté

## Axes d’ordonnancement à tester (dans cet ordre)

1. Expression KRAS (baseline, déjà fait)
2. VAF KRAS (si récupérable pour ≥ 100 patients)
3. Pureté ESTIMATE (croissant et décroissant)
4. Expression MUC16 elle-même (test de cohérence interne)
5. Expression CEACAM5 elle-même

## Flux cibles prioritaires

Panel minimal : MUC16, CEACAM5, + 8–10 flux de contexte (différenciation, immunitaire, stroma) déjà utilisés en v4, en excluant les gènes de pureté/sexe si non corrigés.

## Contrôles obligatoires

- Nul permuté (graine 42) pour chaque axe
- Au moins une rotation de contrôle (ex. pureté comme contrôle, ou un flux non lié)
- Rapport explicite de la pureté moyenne pré/post seuil

## Critères de rétention (rappel)

Le signal n’est retenu que s’il survit au nul **et** à la rotation **et** à au moins une couche orthogonale (survie indépendante de pureté, ou protéine CPTAC, ou CRISPR).

## Sorties attendues

- Cascades + L7a/L7b pour chaque axe
- Table de comparaison réel vs nul
- Association survie (Cox univarié + ajusté pureté si possible)
- Verdict : retenu / exploratoire / rejeté + justification

## Ce qui n’est pas dans ce protocole

- Modification du code v6.2
- Nouveaux criblages médicaments
- Affirmation clinique

---

**Gelé.** Toute modification ultérieure doit créer un P2-PROTO-001b et documenter le delta.
