# Construction matrice enrichie — 19 novembre 2026

## Fait

- Téléchargement Firehose PAAD RSEM (MD5 `b09569ce3f4721f514bc137bd109ac0a` ✓)
- Téléchargement Firehose PAAD GISTIC (MD5 `816034f742e8f89ca8734ca2cf4404d5` ✓)
- Matrice `data/tcga_enriched_p2.csv` : 179 × 23
- SHA256 : `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`
- MTAP-del : 43/177 | kras_fort : 12
- Signal KRAS–MUC16 / KRAS–CEACAM5 reproduit

## Restauration depuis le dépôt

```bash
python scripts/restore_tcga_enriched_p2.py
# vérifie le SHA256 automatiquement
```

## Prêt pour

P2-PROTO-001 / 002 et runs v6.2
