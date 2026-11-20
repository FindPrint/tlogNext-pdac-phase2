# P2.19 — Allèle KRAS et survie

Question : le lien ARN KRAS → CEACAM5 est-il un effet de l'allèle (G12D, G12V, G12R), et est-ce que ce résidu sépare la survie ?

## Sources

- Matrice `data/tcga_enriched_p2` reconstruite depuis `data/b64_chunks` (179 tumeurs).
- Mutations et clinique : cBioPortal datahub, étude `paad_tcga` (`data_mutations.txt`, `data_clinical_patient.txt`), téléchargées le 20 novembre 2026.
- Table jointe : `data/joined_kras_allele_survival.csv`.

Un échantillon sans ligne missense KRAS dans ce fichier est codé `no_missense_call` (n = 42). Ce n'est pas un KRAS sauvage prouvé. Beaucoup de ces cas ne sont simplement pas dans la cohorte de mutations de ce fichier.

## Allèle et expression

Parmi G12D (61), G12V (41) et G12R (25), aucun écart sur :

| Mesure | Kruskal-Wallis p |
|---|---|
| CEACAM5 (log2) | 0,78 |
| ARN KRAS | 0,51 |
| proxy classique (CLDN18, REG4, DPCR1, PGC) | 0,33 |
| CEA après retrait du proxy classique | 0,80 |

L'allèle ne porte pas le signal CEA. G12D, G12V et G12R ont le même niveau de CEA.

## Le dosage d'ARN reste, à l'intérieur des mutants

| Sous-groupe | n | corrélation ARN KRAS vs CEA | vs CEA résiduel du classique |
|---|---|---|---|
| Tous les missense | 137 | 0,27 (p = 0,0018) | 0,21 (p = 0,015) |
| G12D seul | 61 | 0,19 (p = 0,13) | 0,27 (p = 0,034) |
| G12V seul | 41 | 0,33 (p = 0,034) | 0,14 (p = 0,38) |
| G12R seul | 25 | 0,21 (p = 0,32) | 0,26 (p = 0,21) |

Chez les porteurs d'une mutation déjà identifiée, la quantité d'ARN KRAS est encore liée à CEA. Ce n'est pas « quel acide aminé en position 12 ». C'est un écart de dosage, ou quelque chose qui voyage avec lui, à l'intérieur d'un gène déjà muté. L'effectif par allèle est trop petit pour dire que G12D est spécial : seul le résidu y passe le seuil, pas le CEA brut.

## Survie (OS, cBioPortal)

| Contraste | n | log-rank p | Cox non ajusté |
|---|---|---|---|
| quart haut d'ARN KRAS vs reste | 45 / 134 | 0,020 | HR 1,64, p = 0,027 |
| résidu CEA (médiane) | 90 / 89 | 0,95 | — |
| G12D vs G12V | 61 / 41 | 0,026 | non ajusté sur le stade |

Cox du quart haut d'ARN KRAS, avec le proxy classique et le stade AJCC : HR 1,49, p = 0,086. Le signal de survie brut ne tient pas dès qu'on ajuste. Le résidu CEA, avec le même ajustement, ne prédit pas la survie (p = 0,29).

Le stade est très déséquilibré (147 stades II sur 179) : l'ajustement est faible, pas une démonstration d'absence d'effet.

## Lecture pour la suite

1. CEA n'est pas un marqueur de l'allèle KRAS.
2. Le lien qui reste est un lien de dosage d'ARN, partiellement indépendant du programme classique, y compris chez des tumeurs déjà mutées.
3. Ce résidu ne sépare pas les patients qui meurent de ceux qui vivent. Il ne peut pas, en l'état, servir de critère pour un essai.
4. Le prochain pas utile est un score de Moffitt calculé sur le transcriptome entier (pas quatre gènes), puis un Cox avec ce score. Pas un nouveau passage du pipeline de complexité.
