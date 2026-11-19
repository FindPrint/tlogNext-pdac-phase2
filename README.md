# PDAC Phase 2 — Recentrage et pistes prioritaires

**Dépôt phase 2** (19 nov. 2026) — séparé des archives v6.0–v6.2.

**Archives :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)  
**Ce dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)

---

## État au 19 novembre 2026 (fin de journée)

### Matrice enrichie
- `data/tcga_enriched_p2.csv` — **179 × 23**
- SHA256 : `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`
- Sources Firehose vérifiées (RSEM MD5 `b09569ce…`, GISTIC MD5 `816034f7…`)
- Restauration : `python scripts/restore_tcga_enriched_p2.py` (payload embarqué)

### Signal confirmé (P2-PROTO-001 lite)
| Test | Résultat |
|------|----------|
| KRAS ↔ MUC16 | ρ=0,28 p=1,6×10⁻⁴ |
| KRAS ↔ CEACAM5 | ρ=0,34 p=2,8×10⁻⁶ |
| kras_fort → MUC16/CEACAM5 ↑ | p=0,014 / 0,006 |
| **MTAP-del → MUC16/CEACAM5 ↑** | p=0,011 / 0,004 (exploratoire) |

### Objectifs phase 2
1. Stratification CA125/CEA chez KRAS élevé
2. Contexte MTAP / PRMT5 / vopimetostat + daraxonrasib
3. Axes plus légitimes + critères de rétention stricts (nul + rotation + orthogonalité)
4. Livre blanc vivant

### Structure
```
├── README.md
├── livre-blanc/livre-blanc-phase2.md
├── protocols/   (P2-PROTO-001, 002, P2-BUILD-001)
├── data/        (mtap_gistic_status, matrice enrichie)
├── provenance/
├── results/     (tests directs, verdicts)
└── scripts/     (prepare, restore, merge)
```

### Avancement
- [x] Dépôt + plan + protocoles
- [x] Matrice enrichie Firehose
- [x] Tests directs lite (signal CA125/CEA + MTAP exploratoire)
- [ ] Pureté ESTIMATE
- [ ] Runs UNIVERSAL_LOG v6.2 (cascades + nuls + rotations)
- [ ] Validation externe GEO

Travail bénévole, non clinique, données publiques. Aucune promesse thérapeutique.
