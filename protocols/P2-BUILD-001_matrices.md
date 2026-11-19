# P2-BUILD-001 — Construction des matrices enrichies (TCGA)

**Statut :** gelé le 19 novembre 2026  
**Lié à :** P2-PROTO-001, P2-PROTO-002  
**Script :** `scripts/prepare_enriched_tcga_matrix.py`

---

## Objectif

Produire un CSV unique, traçable, prêt pour les runs v6.2 de la phase 2, contenant :

| Colonne | Source | Usage |
|---------|--------|-------|
| MUC16, CEACAM5, KRAS, + panel | Expression Firehose / matrices archives | Flux + cibles |
| mtap_del | mtap_gistic_status.csv (archives, GISTIC -2) | Axe / strate P2-PROTO-002 |
| purity_estimate | ESTIMATE (TCGA-PAAD) | Axe / covariable |
| kras_vaf | MAF TCGA (si disponible) | Axe prioritaire |
| kras_rank, purity_rank, muc16_rank, … | Dérivés | Contrôles ordonnés |

## Sources (rappel provenance archives)

- Expression : Broad GDAC Firehose stddata 2016-01-28 PAAD, MD5 `b09569ce…`
- GISTIC MTAP : `mtap_gistic_status.csv` (SHA `b54cb94f…`), 177 tumeurs appariées
- Pureté : scores ESTIMATE TCGA (Aran et al. / Yoshihara) ou fichier local déjà utilisé en v3/v4
- VAF KRAS : MAF cBioPortal / GDC (à récupérer si pas déjà local)

## Commande type

```bash
python scripts/prepare_enriched_tcga_matrix.py \
  --expression /chemin/vers/expression_matrix_or_fluxes.csv \
  --mtap-gistic /chemin/vers/mtap_gistic_status.csv \
  --purity /chemin/vers/estimate_purity_paad.csv \
  --kras-maf /chemin/vers/paad_mutations.maf \
  --output data/tcga_enriched_p2.csv
```

Le script imprime les SHA de chaque entrée et de la sortie. Ces SHA doivent être reportés dans `provenance/` avant tout run.

## Règles

- Aucune imputation de VAF ou de pureté manquante.
- Les samples sans MTAP GISTIC sont marqués mtap_del = False seulement si la colonne est absente ; sinon NaN → exclu des analyses stratifiées MTAP.
- Le script ne lance pas le pipeline ; il prépare uniquement l’entrée.

## Prochaine étape après construction

1. Vérifier n, distributions (MUC16, CEACAM5, KRAS, purity, VAF, % MTAP-del).
2. Geler le SHA de `tcga_enriched_p2.csv` dans `provenance/PROVENANCE_tcga_enriched_p2.md`.
3. Lancer P2-PROTO-001 (axes dans l’ordre du protocole).

---

**Gelé.**
