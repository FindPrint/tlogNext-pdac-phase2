# PDAC Phase 2 — Recentrage et pistes prioritaires

**Dépôt phase 2** (19 nov. 2026) — séparé des archives v6.0–v6.2.

**Archives :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)  
**Ce dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)

---

## État au 19 novembre 2026 (soir)

### Matrice enrichie — **RESTAURABLE**
```bash
python scripts/restore_tcga_enriched_p2.py
# → data/tcga_enriched_p2.csv
#   179 × 24 | SHA256 6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd
```
- Payload : `data/b64_chunks/chunk_00.txt` … `chunk_08.txt` (vérifiés, reconstruction OK)
- Sources Firehose RSEM + GISTIC (MD5 vérifiés)
- Colonnes : expression log2 (MUC16, CEACAM5, KRAS, MTAP, CDKN2A, PRMT5…) + ranks + mtap_del / cdkn2a_del + kras_fort

### Signaux confirmés (P2.4 → P2.6)
| Test | Résultat |
|------|----------|
| KRAS ↔ MUC16 | ρ=0,28 p=1,6×10⁻⁴ |
| KRAS ↔ CEACAM5 | ρ=0,34 p=2,8×10⁻⁶ |
| MTAP-del → CEACAM5 | **Cohen d=+0,53** p=0,003 |
| MTAP-del → MUC16 | **Cohen d=+0,46** p=0,010 |
| Résidus KRAS (CEA) | p=0,011 (survit) |
| Résidus KRAS (CA125) | p=0,023 (survit) |

### Objectifs phase 2
1. Stratification CA125/CEA chez KRAS élevé
2. Contexte MTAP / PRMT5 / vopimetostat + daraxonrasib
3. Axes légitimes + critères stricts (nul + rotation + orthogonalité)
4. Livre blanc vivant

### Structure
```
├── README.md
├── livre-blanc/livre-blanc-phase2.md   ← P2.6 à jour
├── protocols/
├── data/b64_chunks/                    ← payload matrice
├── data/mtap_gistic_status.csv
├── provenance/
├── results/                            ← verdicts + tables
└── scripts/restore_tcga_enriched_p2.py
```

### Avancement
- [x] Dépôt + plan + protocoles
- [x] Matrice enrichie Firehose + **restore fonctionnel**
- [x] Tests directs + residualisation + stratification KRAS
- [ ] Pureté ESTIMATE
- [ ] Runs UNIVERSAL_LOG v6.2 (cascades + nuls + rotations)
- [ ] Validation externe GEO

Travail bénévole, non clinique, données publiques. Aucune promesse thérapeutique.
