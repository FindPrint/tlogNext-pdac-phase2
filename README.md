# PDAC Phase 2 — Recentrage et pistes prioritaires

**Dépôt phase 2** (19 nov. 2026)

**Archives :** [tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)  
**Ce dépôt :** [tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)

---

## État (19 nov 2026 soir)

### Signal retenu
**kras_high (Q4 expression KRAS) → CEA plus élevé**

| Cohort | n | Cohen d | null_p |
|--------|---|---------|--------|
| TCGA-PAAD (après pureté) | 178 | +0,34 | 0,054 |
| **GSE71729** | 145 | **+0,52** | **0,008** |
| **GSE62452** | 69 | **+0,68** | **0,019** |

Validation externe **positive**. MTAP et KRAS continu non retenus après pureté.

### Documents
- Livre blanc : `livre-blanc/livre-blanc-phase2.md` (P2.10)
- `results/P2_010_GEO_validation.md`
- `results/P2_009_retention_nulls.md`
- `results/P2_011_targeted_v6_style.md`

### Matrice
```bash
python scripts/restore_tcga_enriched_p2.py
```

### Avancement
- [x] Matrice + pureté + rétention nuls
- [x] Validation GEO (GSE71729 + GSE62452)
- [x] Négatifs honnêtes (MTAP, KRAS continu)
- [ ] Run UNIVERSAL_LOG v6.2 full ciblé (axe kras_high)
- [ ] ESTIMATE en complément

Travail bénévole, non clinique, données publiques.
