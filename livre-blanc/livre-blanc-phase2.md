# Livre blanc — PDAC Phase 2

**Document vivant** — mis à jour à chaque étape (fait / testé / pensé / analysé / connu / inconnu).  
**Dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)  
**Archives (v6.0–v6.2, §1–§8.42) :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)

**Règle de provenance (permanente) :** chaque donnée, chaque résultat, chaque affirmation porte sa source complète, la nature des lignes, comment chaque valeur a été produite, les hachages, et ce qui manque.

**Règle d’honnêteté (permanente) :** ce document ne présente jamais une piste comme un remède, ni un seuil comme une preuve clinique. Un résultat négatif est un résultat.

---

## P2.0 — Pourquoi un nouveau dépôt et un recentrage

Date : 19 novembre 2026.

Le travail des 15–19 novembre 2026 (dépôt d’archives) a produit :
- Un instrument fiable (v6.2, gigue L5 = 0).
- Un signal d’expression robuste : KRAS élevé ↔ CA125 (MUC16) / CEA élevés, avec lien de survie pour CA125.
- Une piste clinique réelle hors pipeline (daraxonrasib ; combinaison vopimetostat + daraxonrasib chez MTAP-délétés avec appui PRMT5).
- Beaucoup de négatifs solides (différenciation pureté-dépendante, CRISPR/médicaments négatifs, protéine non confirmatoire, Delta/MC non discriminants).

Continuer à tourner des versions du même pipeline sur les mêmes axes (rang KRAS, pureté) risquait de diluer l’attention et de mélanger archives et travail de suite. Ce dépôt isole la **phase 2** : recentrage sur ce qui tient, axes plus légitimes, critères de rétention plus stricts, livre blanc vivant dédié.

---

## P2.1 — Plan d’attaque prioritaire et critères de décision

Date : 19 novembre 2026.

### Objectif opérationnel

Produire **2 à 4 hypothèses** de biomarqueur de stratification ou de combinaison / fenêtre thérapeutique, avec le plus fort niveau de preuve orthogonal possible (expression + CRISPR + sensibilité médicament + survie + contrôle de pureté).

### Priorités

1. Stratification **CA125 (MUC16) / CEA** chez KRAS élevé  
2. Contexte **MTAP-délété / PRMT5 / vopimetostat + daraxonrasib**  
3. ATR en surveillance seulement  
4. Autres uniquement si un nouvel axe les réactive

### Critères de rétention (stricts)

Un signal n’est retenu que s’il survit au **nul permuté** ET à la **rotation des contrôles** ET à **au moins une couche orthogonale** (protéine, CRISPR, sensibilité médicament, ou survie indépendante de pureté).

---

## P2.2 — Inventaire des axes et variables réellement disponibles

Axes immédiatement actionnables :
1. VAF / expression KRAS  
2. Statut MTAP (GISTIC -2)  
3. Pureté ESTIMATE (TCGA-PAAD)

Sources : TCGA-PAAD, CPTAC, DepMap 24Q4, GEO GSE71729/GSE62452, ICGC.  
Détail dans `provenance/INVENTAIRE_AXES_2026-11-19.md`.

---

## P2.3 — Préparation des matrices enrichies (en cours)

Date : 19 novembre 2026.

### Fait

- Script `scripts/prepare_enriched_tcga_matrix.py` : charge expression + MTAP GISTIC + pureté ESTIMATE + VAF KRAS, produit `data/tcga_enriched_p2.csv` avec colonnes de rang pour les axes.
- Protocole de construction gelé : `protocols/P2-BUILD-001_matrices.md`.
- Provenance de préparation : `provenance/PROVENANCE_preparation_matrices.md`.

### En attente (nécessite les fichiers locaux / téléchargements)

- Exécution réelle du script sur les matrices Firehose + `mtap_gistic_status.csv` (archives) + pureté ESTIMATE + MAF KRAS.
- Écriture des SHA d’entrée et de sortie dans la provenance.
- Vérification des distributions (n, % MTAP-del, couverture VAF, etc.).

### Ensuite

Lancement de P2-PROTO-001 (axes dans l’ordre du protocole) dès que la matrice enrichie est gelée.

---

## Journal phase 2

| Date | Action | Résultat / note |
|------|--------|-----------------|
| 19 nov. 2026 | Création dépôt `tlogNext-pdac-phase2` | Séparation archives / phase 2 |
| 19 nov. 2026 | P2.0 + P2.1 | Plan d’attaque + critères de rétention |
| 19 nov. 2026 | P2.2 + PROTO-001/002 | Inventaire axes + protocoles gelés |
| 19 nov. 2026 | P2.3 + script + BUILD-001 | Préparation matrices enrichies documentée et scriptée |

---

*Les sections suivantes (résultats des runs, verdicts) seront ajoutées au fur et à mesure.*
