# P2-PROTO-002 — Contexte MTAP-délété / PRMT5 / lien éventuel avec CA125-CEA

**Statut :** gelé le 19 novembre 2026  
**Priorité :** 2 (piste clinique la plus solide)  
**Instrument :** UNIVERSAL_LOG v6.2 (Cohen-d)

---

## Question

Le groupe MTAP-délété (déjà distingué par dépendance PRMT5 plus forte, p=0,0036) présente-t-il des régimes d’expression distincts (notamment autour de MUC16/CEACAM5 ou d’autres flux) lorsqu’on ordonne par statut MTAP ou par axes associés ? Existe-t-il un signal orthogonal qui renforce ou nuance le rationnel vopimetostat + daraxonrasib ?

## Contexte déjà établi (archives §8.40)

- Dépendance PRMT5 plus forte en lignées pancréas MTAP-délétées (reproduit).
- Aucun écran médicament (PRISM/GDSC) ne distingue le groupe (vopimetostat absent des bibliothèques).
- Lien KRAS non significatif (Fisher p=0,073).
- L’effet suit MTAP, pas seulement CDKN2A (4 confirmations).

## Données

- TCGA-PAAD : statut MTAP inféré par deep deletion 9p21 (GISTIC/CNA) + expression
- DepMap : lignées avec statut MTAP + scores Chronos (déjà utilisé)
- CPTAC : si statut MTAP/CDKN2A disponible

## Axes d’ordonnancement

1. Statut MTAP binaire (délété vs intact) — ordre forcé ou analyse de groupe
2. Expression KRAS ou VAF KRAS à l’intérieur des MTAP-délétés vs intacts
3. Pureté ESTIMATE

## Flux prioritaires

- MUC16, CEACAM5 (lien éventuel avec le signal priorité 1)
- PRMT5 et gènes de la voie méthionine/salvage si disponibles
- Panel immunitaire / stroma déjà exploré

## Contrôles obligatoires

- Nul permuté
- Comparaison MTAP-délété vs intact (pas seulement un scan de seuil)
- Rapport de la co-occurrence CDKN2A

## Critères de rétention

Identiques à P2.1 (nul + rotation ou justification + orthogonalité).

## Sorties attendues

- Différences d’expression / cascades entre MTAP-délété et intact
- Lien éventuel avec CA125/CEA
- Verdict clair sur la valeur ajoutée pour la piste clinique existante

## Ce qui n’est pas dans ce protocole

- Nouveaux essais cliniques
- Affirmation que le pipeline « valide » vopimetostat

---

**Gelé.** Toute modification ultérieure doit créer un P2-PROTO-002b.
