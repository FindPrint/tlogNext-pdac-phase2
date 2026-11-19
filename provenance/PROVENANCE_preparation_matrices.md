# Provenance — Préparation matrices phase 2

Date : 19 novembre 2026

## Script

- `scripts/prepare_enriched_tcga_matrix.py`
- Protocole : `protocols/P2-BUILD-001_matrices.md`

## Sources réutilisées (archives)

| Élément | Référence archives | SHA / MD5 |
|---------|-------------------|-----------|
| Expression Firehose PAAD | PROVENANCE_tcga.md / Firehose 2016-01-28 | MD5 `b09569ce…` |
| mtap_gistic_status.csv | PROVENANCE_mtap.md | SHA `b54cb94ff6aaba67e71524476d4e47c567f20ca8d49c09c52a9118977a7c38cb` |
| Définition MTAP-del | GISTIC -2 (délétion profonde) | — |
| Pureté ESTIMATE | Aran et al. Nat Commun 2015 ; Yoshihara et al. 2013 | À reporter lors du run réel |
| VAF KRAS | MAF TCGA / cBioPortal | À reporter lors du run réel |

## Règle

Les SHA des fichiers d’entrée réellement utilisés lors de la construction de `data/tcga_enriched_p2.csv` doivent être écrits ici (ou dans un fichier dédié) **avant** le premier run P2-PROTO-001. Aucun run sans provenance complète des entrées.
