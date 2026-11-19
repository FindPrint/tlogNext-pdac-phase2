# Provenance — tcga_enriched_p2.csv

**Date de construction :** 19 novembre 2026  
**SHA256 :** `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`  
**Shape :** 179 échantillons × 23 colonnes  

## Sources

| Fichier | MD5 | URL |
|---------|-----|-----|
| Firehose PAAD RSEM tar.gz | `b09569ce3f4721f514bc137bd109ac0a` | gdac.broadinstitute.org stddata__2016_01_28 PAAD |
| Firehose PAAD GISTIC tar.gz | `816034f742e8f89ca8734ca2cf4404d5` | gdac.broadinstitute.org analyses__2016_01_28 PAAD |

## Transformations

1. Expression : log2(RSEM normalisé + 1), tumeurs primaires code 01 (179).
2. Gènes : MUC16, CEACAM5, KRAS, PGC, CLDN18, REG4, KRT20, DPCR1, CLCA1, MUC2, MUC17, GSTM1, PRMT5, MTAP, CDKN2A.
3. MTAP-del : GISTIC == -2 (43 / 177 non-NA).
4. kras_fort : 12 tumeurs à plus forte expression KRAS.
5. Rangs : average rank sur KRAS, MUC16, CEACAM5.

## Vérifications rapides

- Spearman KRAS vs MUC16 : rho ≈ 0,279, p ≈ 1,6e-4
- Spearman KRAS vs CEACAM5 : rho ≈ 0,342, p ≈ 2,8e-6
- Parmi kras_fort : MTAP-del 6/12

Note : 179 vs 178 archives (filtre -01). Pas de correction pureté dans cette version de base.
