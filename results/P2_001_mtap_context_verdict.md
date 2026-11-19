# P2-PROTO-001 / MTAP context — verdict étendu (2026-11-19)

**Matrice** : `tcga_enriched_p2.csv` (n=179, SHA256 `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`)
**Source GISTIC** : Firehose PAAD MTAP (del = GISTIC −2)

## Signaux principaux

| Axis | n_wt / n_del | Cohen d (del vs wt) | MW p |
|------|--------------|---------------------|------|
| ceacam5_rank | 136 / 43 | **+0.53** | 0.0033 |
| muc16_rank | 136 / 43 | **+0.46** | 0.010 |
| CEACAM5_log2 | 136 / 43 | +0.52 | 0.0033 |
| MUC16_log2 | 136 / 43 | +0.35 | 0.010 |
| kras_rank | 136 / 43 | +0.26 | 0.13 (ns) |
| MTAP_log2 | 136 / 43 | **−1.49** | 2.5e-12 |
| CDKN2A_log2 | 136 / 43 | **−1.46** | 7e-14 |
| PRMT5_log2 | 136 / 43 | −0.02 | 0.83 (ns) |

## Residualisation KRAS
- residual muc16_rank ~ mtap_del : Spearman r = 0.169, p = 0.023
- residual ceacam5_rank ~ mtap_del : Spearman r = 0.190, p = 0.011

→ Le signal MTAP → CA125/CEA **survit** à la residualisation par KRAS rank.

## Fisher exact (médiane)
- mtap_del × muc16_high : OR ≈ 2.62, p ≈ 0.0088
- mtap_del × cea_high : OR ≈ 2.62, p ≈ 0.0088

## Interprétation (honnête)
1. **MTAP-del** (co-deletion CDKN2A) est associé à une expression/rank plus élevée de MUC16 (CA125) et CEACAM5 (CEA).
2. L’effet est d’intensité moyenne (Cohen d ~0.45–0.53) et reste significatif après contrôle de KRAS rank.
3. PRMT5 n’est pas différentiellement exprimé (attendu : la vulnérabilité est synthétique, pas d’expression différentielle forte).
4. Le signal KRAS → CA125/CEA (déjà vu en phase 1) et le signal MTAP → CA125/CEA sont **partiellement indépendants**.

## Prochaines étapes prioritaires
- Lancer UNIVERSAL_LOG v6.2 full (nuls + rotations) sur les axes `kras_rank`, `muc16_rank`, `ceacam5_rank`, `mtap_del`.
- Ajouter pureté ESTIMATE si possible.
- Validation externe GEO (GSE71729 / GSE62452).
- Explorer interaction KRAS × MTAP sur le phénotype sécrétoire.

Fichier données : `results/p2_proto001_mtap_extended_2026-11-19.csv`
