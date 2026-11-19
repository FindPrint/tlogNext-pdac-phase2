# Provenance — tcga_enriched_p2.csv

**Date de construction :** 19 novembre 2026  
**SHA256 :** `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`  
**Shape :** 179 échantillons × 23 colonnes  

## Fichiers dans le dépôt

- `data/tcga_enriched_p2_part1.csv` … `_part3.csv` — matrice découpée
- `scripts/merge_enriched_parts.py` — reconstitution
- `data/tcga_enriched_p2.csv.gz.b64` — version gzip+base64 monobloc

```bash
python scripts/merge_enriched_parts.py
# ou :
python -c "import base64,gzip; open('data/tcga_enriched_p2.csv','wb').write(gzip.decompress(base64.b64decode(open('data/tcga_enriched_p2.csv.gz.b64').read())))"
```

## Sources

| Fichier | MD5 | URL |
|---------|-----|-----|
| Firehose PAAD RSEM tar.gz | `b09569ce3f4721f514bc137bd109ac0a` | gdac stddata__2016_01_28 PAAD |
| Firehose PAAD GISTIC tar.gz | `816034f742e8f89ca8734ca2cf4404d5` | gdac analyses__2016_01_28 PAAD |

## Transformations

1. log2(RSEM+1), tumeurs primaires -01 (n=179)
2. Gènes : MUC16, CEACAM5, KRAS, PGC, CLDN18, REG4, KRT20, DPCR1, CLCA1, MUC2, MUC17, GSTM1, PRMT5, MTAP, CDKN2A
3. mtap_del = (GISTIC == -2) → 43/177
4. kras_fort = top-12 KRAS expression
5. Rangs average : kras_rank, muc16_rank, ceacam5_rank

## Vérifications

- Spearman KRAS–MUC16 : ρ≈0.279, p≈1.6e-4
- Spearman KRAS–CEACAM5 : ρ≈0.342, p≈2.8e-6
- kras_fort ∩ MTAP-del : 6/12

Pas de correction pureté dans cette version de base.
