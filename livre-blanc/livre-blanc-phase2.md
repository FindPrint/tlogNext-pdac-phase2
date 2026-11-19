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

Date : 19 novembre 2026. Statut : plan initial, à affiner après inventaire des données disponibles.

### Objectif opérationnel (remplace « trouver un remède »)

Produire **2 à 4 hypothèses** de :
- biomarqueur de stratification, ou
- combinaison / fenêtre thérapeutique,  
avec le **plus fort niveau de preuve orthogonal possible** (expression + CRISPR + sensibilité médicament + survie + contrôle de pureté), documentées de façon traçable et prêtes à être testées ou confrontées aux essais en cours.

### Priorités ordonnées

| Rang | Piste | Justification (état 19 nov. 2026) | Actions phase 2 |
|------|-------|-----------------------------------|-----------------|
| 1 | Stratification **CA125 (MUC16) / CEA** chez KRAS élevé | Signal d’expression 3/4 cohortes ; survie 2/3 cohortes ; lien direct avec le groupe KRAS le plus fort | Construire axes et panels ; tester valeur pronostique / prédictive ; vérifier pureté et orthogonalité |
| 2 | Contexte **MTAP-délété / PRMT5 / vopimetostat + daraxonrasib** | Piste clinique la plus solide (82 % réponses phase 1/2) ; appui dépendance PRMT5 mesuré (p=0,0036) ; 4 confirmations indépendantes MTAP vs CDKN2A | Ordres par statut MTAP ; co-expression ; vulnérabilités associées ; liaison éventuelle avec CA125/CEA |
| 3 | **ATR** (piste ouverte) | Hypothèse d’expression seulement ; pas d’appui CRISPR ni médicament fort à ce stade | Garder en surveillance ; ne pas prioriser de nouveaux runs lourds tant que 1 et 2 ne sont pas stabilisés |
| 4 | Autres (différenciation, immunitaire, réparation ADN…) | Fragiles ou pureté-dépendants ou déjà bien explorés en négatif | Seulement si un nouvel axe légitime les réactive |

### Critères de rétention d’un signal (stricts)

Un signal (seuil, cascade, association) n’est **retenu** comme hypothèse prioritaires que s’il satisfait **les trois** conditions suivantes :

1. **Survie au nul permuté** (même marginales, ordre détruit) — l’écart réel vs nul dépasse la gigue / plancher défini dans le protocole.
2. **Survie à la rotation des contrôles** (ou justification documentée pourquoi la rotation n’est pas applicable).
3. **Au moins une couche orthogonale** : protéine (CPTAC ou autre), dépendance CRISPR (DepMap), sensibilité médicament (PRISM/GDSC ou autre), **ou** association de survie indépendante de la pureté.

Un signal qui échoue à l’un des trois est classé « exploratoire / non retenu » et documenté comme tel.

### Axes d’ordonnancement prioritaires à explorer

Par ordre de légitimité décroissante (à confronter aux données réellement disponibles) :

1. Fraction allélique / dose KRAS (si récupérable depuis TCGA ou autres).
2. Statut MTAP (délété vs intact) + scores associés.
3. Scores de pureté + sous-type moléculaire (basal vs classical) + stade.
4. Ordre par expression de CA125 ou CEA (pour tester la cohérence interne du signal).
5. Ordre par sensibilité à un médicament de référence (ex. proxy pan-RAS ou ATR si données disponibles).
6. Scores de progression clinique ou temps jusqu’à événement (quand les données le permettent).

Le simple « rang KRAS croissant » reste utilisable comme baseline, mais n’est plus l’axe par défaut unique.

### Règles de travail phase 2

- Tout protocole est **gelé avant le run** (fichier dans `protocols/`).
- Chaque run porte son SHA de code, de données, ses graines, sa commande exacte.
- Les résultats (positifs **et** négatifs) sont écrits dans `results/` et résumés dans le livre blanc.
- Le pipeline v6.2 n’est pas modifié ici ; les améliorations éventuelles du code restent dans le dépôt d’archives ou un dépôt Code dédié.
- Transparence : ce dépôt est public.

### Prochaines étapes concrètes (ordre proposé)

1. Inventaire précis des colonnes / variables disponibles pour les axes prioritaires (TCGA, CPTAC, DepMap, GEO, ICGC…).  
2. Rédaction de 2–3 protocoles gelés (P2-PROTO-001 et suivants).  
3. Construction des matrices / CSV nécessaires.  
4. Premier lot de runs + nuls + rotations.  
5. Verdict selon les critères de rétention ci-dessus.  
6. Mise à jour du livre blanc et du README.

---

## P2.2 — Inventaire des axes et variables réellement disponibles (19 novembre 2026)

### Sources principales déjà utilisées ou accessibles

| Source | Type | n approximatif | Variables clés pour phase 2 | Notes / limites |
|--------|------|----------------|-----------------------------|-----------------|
| **TCGA-PAAD** (Firehose / cBioPortal / GDC) | ARN + mutations + CNA + clinique | ~178 tumeurs primaires | Expression MUC16, CEACAM5, KRAS ; mutations KRAS (dont VAF dans les MAF) ; CNA 9p21 (MTAP/CDKN2A) ; pureté ESTIMATE / CPE ; survie ; stade | Biais résécable (stade IIB dominant). Pureté ESTIMATE disponible (RNA-seqV2). KRAS VAF récupérable depuis les appels mutation. |
| **CPTAC PDAC** (Cao et al. Cell 2021) | Protéome + phospho + ARN + WES | 140 tumeurs (105 haute cellularité) | KRAS VAF (cutoff 0,075 utilisé pour pureté) ; expression protéique éventuelle MUC16/CEACAM5 ; statut MTAP/CDKN2A | Excellent pour orthogonalité protéique. Déjà partiellement exploré. |
| **DepMap 24Q4** | CRISPR Chronos + lignées | ~45 lignées pancréas | Dépendance PRMT5, ATR, etc. ; statut MTAP des lignées | Déjà utilisé pour l’arbitrage MTAP/PRMT5 (p=0,0036). |
| **GEO GSE71729 / GSE62452** | Expression (puce) | 145 / 69 | Expression MUC16, CEACAM5, KRAS | Validation externe du signal CA125/CEA. |
| **ICGC** | Expression + clinique | ~70 | Survie, expression | Signal CA125 de survie déjà vu ; expression moins claire. |

### Axes prioritaires — disponibilité concrète

1. **Fraction allélique / dose KRAS**  
   - Disponible : VAF KRAS dans les fichiers de mutations TCGA (MAF) et CPTAC.  
   - Dosage mutant (copies du mutant) plus élaboré existe dans la littérature récente (Nature Medicine 2025) mais demande pureté + CNA + VAF.  
   - **Utilisable immédiatement** comme axe continu (VAF) ou binaire (haut vs bas VAF).

2. **Statut MTAP**  
   - Inférable par deep deletion 9p21 (GISTIC / CNA) — très corrélé à CDKN2A.  
   - Prévalence PDAC ~20–28 %.  
   - Déjà partiellement arbitré (§8.40 archives).  
   - **Utilisable immédiatement** comme contrôle binaire (délété vs intact).

3. **Pureté tumorale**  
   - ESTIMATE (stromal + immune → pureté) disponible pour TCGA-PAAD RNA-seqV2 (n≈179).  
   - CPE (consensus) et ABSOLUTE partiellement disponibles.  
   - CPTAC a utilisé KRAS VAF ≥ 0,075 comme proxy de cellularité.  
   - **Déjà utilisé** dans les versions v3/v4 du projet ; à réutiliser systématiquement comme covariable ou axe.

4. **Sous-type moléculaire (basal / classical)**  
   - Calculable à partir de l’expression (signatures Moffitt ou Bailey).  
   - Disponible dans plusieurs publications TCGA/CPTAC.  
   - **À construire** si pas déjà présent dans les matrices locales.

5. **Ordre par CA125 (MUC16) ou CEA**  
   - Directement disponible dans toutes les matrices d’expression déjà utilisées.  
   - Utile pour tester la cohérence interne du signal (si on ordonne par MUC16, les autres flux du panel se comportent-ils de façon cohérente ?).

6. **Sensibilité médicament**  
   - PRISM / GDSC disponibles via DepMap ; vopimetostat absent des bibliothèques testées (§8.40).  
   - Pas d’axe « sensibilité daraxonrasib » public à ce jour (médicament trop récent).

### Conclusion de l’inventaire

Les trois axes les plus légitimes et immédiatement actionnables sont :
1. **VAF / expression KRAS** (continuum)
2. **Statut MTAP** (binaire, CNA)
3. **Pureté ESTIMATE** (continuum) + éventuel sous-type

CA125/CEA restent les cibles prioritaires de stratification.

---

## Journal phase 2

| Date | Action | Résultat / note |
|------|--------|-----------------|
| 19 nov. 2026 | Création du dépôt `tlogNext-pdac-phase2` | Séparation claire archives / phase 2 |
| 19 nov. 2026 | Rédaction P2.0 + P2.1 | Plan d’attaque et critères de rétention publiés |
| 19 nov. 2026 | Rédaction P2.2 + protocoles 001/002 | Inventaire axes + premiers protocoles gelés |

---

*Les sections suivantes seront ajoutées au fur et à mesure des runs et des verdicts.*
