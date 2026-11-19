# PDAC Phase 2 — Recentrage et pistes prioritaires

**Nouveau dépôt** créé le 19 novembre 2026 pour ne pas mélanger le travail de suite avec les archives v6.0–v6.2.

**Dépôt d’archives (ne plus pousser de nouveau contenu principal) :**  
[FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac) — livre blanc jusqu’au §8.42, pipeline v6.2, provenances et résultats des 15–19 novembre 2026.

**Ce dépôt :** travail de phase 2. Objectif opérationnel resserré : produire 2–4 hypothèses de combinaison / biomarqueur / fenêtre thérapeutique avec le plus fort niveau de preuve orthogonal possible (expression + dépendance CRISPR + sensibilité médicament + survie + pureté), en utilisant UNIVERSAL_LOG v6.2 comme instrument de détection de régimes, pas comme moteur de découverte de remède.

---

## État consolidé au 19 novembre 2026 (issu des archives)

### Signaux qui tiennent
- Groupe KRAS le plus élevé → **CA125 (MUC16)** et **CEA (CEACAM5)** élevés. Confirmé en expression dans **3 cohortes sur 4** (TCGA, GSE71729, GSE62452 ; ICGC non). CA125 prédit une survie plus courte dans **2 cohortes sur 3** (TCGA Cox univarié 1,44 ; ICGC quartile 9,5 vs 23,8 mois, p=0,002, Cox 1,57).
- **Daraxonrasib** (pan-RAS) : double la survie médiane en phase III (13,2 vs 6,7 mois, HR 0,40) — avance clinique réelle hors pipeline.
- **Piste la plus solide du projet :** vopimetostat + daraxonrasib chez les patients **MTAP-délétés** (82 % de réponses, 18/22, phase 1/2 non randomisée ; phase 3 prévue 1er semestre 2027). Appui mesuré : dépendance PRMT5 plus forte en pancréas (p=0,0036). L’effet suit MTAP, pas CDKN2A (4 confirmations indépendantes).
- ATR : seule piste ouverte purement d’expression (sans appui CRISPR ni médicament fort).

### Ce qui ne tient pas ou est fragile
- Effondrement des marqueurs de différenciation (PGC, DPCR1, CLDN18…) dépendant de la pureté et de la cohorte.
- CRISPR (DepMap) et criblages médicaments (PRISM / GDSC) négatifs sur les cibles testées dans le pipeline.
- Chaîne non confirmée en protéine (CPTAC).
- S_sep / max_separation séparent le réel du nul sur les rotations ordonnées par construction (48/48), mais ne prouvent pas de rupture biologique.
- Delta et MC ne séparent pas de façon fiable le réel du nul sur la plupart des paires.

### Instrument
- UNIVERSAL_LOG **v6.2** (Cohen-d, hachage L5 stable, gigue 0) est la version de travail. Code et protocoles dans le dépôt d’archives.
- Le pipeline détecte des seuils et cascades dans des séries ordonnées. Il ne trouve pas un remède. Il peut pointer des cibles et combinaisons à tester ensuite.

---

## Objectifs de la phase 2 (opérationnels)

1. **Stratification biomarqueur** autour de CA125/MUC16 et CEA chez les tumeurs à KRAS élevé (et test de valeur ajoutée pour les patients candidats aux pan-RAS).
2. **Appui / contexte** autour de la piste clinique vopimetostat + daraxonrasib (MTAP / PRMT5) : ordres, co-expression, vulnérabilités associées.
3. **Axes d’ordonnancement plus légitimes** que le simple rang KRAS ou pureté (fraction allélique si disponible, scores de pureté + sous-type, ordre par sensibilité médicament de référence, scores de progression clinique).
4. **Critères de rétention stricts** : un signal n’est retenu que s’il survit au nul permuté **et** à la rotation des contrôles **et** à au moins une couche orthogonale (protéine ou CRISPR ou survie).
5. **Livre blanc vivant** : chaque décision, protocole, résultat (positif ou négatif) est documenté avec provenance complète.

Aucune promesse clinique. Un résultat négatif est un résultat.

---

## Structure du dépôt

```
├── README.md                 # ce fichier
├── livre-blanc/              # source Markdown du livre blanc phase 2
│   └── livre-blanc-phase2.md
├── protocols/                # protocoles gelés avant chaque run
│   ├── P2-PROTO-001_CA125_stratification.md
│   └── P2-PROTO-002_MTAP_context.md
├── provenance/               # sources, hachages, nature des lignes
├── results/                  # sorties des runs, tables, verdicts
├── scripts/                  # scripts d’extraction, construction, analyse
└── sections/                 # sections numérotées prêtes à insérer
```

Le code du pipeline UNIVERSAL_LOG reste dans le dépôt d’archives (et éventuellement un dépôt Code séparé). Ce dépôt phase 2 se concentre sur le travail scientifique PDAC, les protocoles, les résultats et le livre blanc.

---

## Avancement

- [x] Création du dépôt et structure initiale
- [x] P2.1 — Plan d’attaque prioritaire et critères de décision
- [x] P2.2 — Inventaire des axes et variables réellement disponibles
- [x] Protocoles gelés P2-PROTO-001 (CA125/CEA) et P2-PROTO-002 (MTAP)
- [ ] Construction des matrices enrichies (VAF KRAS, pureté ESTIMATE, statut MTAP)
- [ ] Premier lot de runs phase 2 + nuls + rotations
- [ ] Verdicts selon critères de rétention + mise à jour livre blanc

---

**Mandat d’origine (Zackary, 15–16 nov. 2026) :** chercher des pistes thérapeutiques contre le PDAC avec le pipeline, maintenir un livre blanc de tout ce qui est fait / testé / pensé / analysé / connu / inconnu, continuer jusqu’à ce qu’une piste solide émerge.  
**Règle permanente :** traçable, reproductible, clair, public. Le pipeline lui-même n’est pas commercialisé.

Travail bénévole, non clinique, sur données publiques.
