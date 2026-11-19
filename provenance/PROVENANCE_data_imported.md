# Provenance — Données importées depuis les archives (19 nov. 2026)

## Fichiers importés dans ce dépôt

| Fichier | Source archives | SHA (blob GitHub) | Contenu |
|---------|-----------------|-------------------|--------|
| `data/mtap_gistic_status.csv` | `tlogNext-cancer-pdac/data_flux/mtap_gistic_status.csv` | `fb1d03ecb457a50168d2a5ab086ae3364a70b12e` | 178 lignes (barcode, sample15, mtap_gistic, cdkn2a_gistic, kras_fort). GISTIC −2 = délétion profonde. |

## Définition MTAP-del (inchangée)

- `mtap_del = (mtap_gistic == -2)`
- Une ligne a des NaN GISTIC (TCGA-FB-A4P6) — à exclure des analyses stratifiées MTAP (comme en §8.26/§8.40).

## Ce qui manque encore pour P2-PROTO-001 complet

- Matrice d’expression avec **MUC16** et **CEACAM5** (et panel contexte) pour les 178 tumeurs.
- Les matrices de flux v4 des archives contiennent ces gènes mais ne sont pas toutes poussées en CSV léger dans `data_flux/`.
- Pureté ESTIMATE et VAF KRAS (MAF) restent à récupérer via `DATA_SOURCES.md` des archives.

## Prochaine étape

Joindre l’expression MUC16/CEACAM5 dès qu’une matrice complète est disponible, puis lancer P2-PROTO-001.
