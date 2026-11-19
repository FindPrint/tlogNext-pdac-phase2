# PDAC Phase 2 — Recentrage et pistes prioritaires

**Dépôt phase 2** (19 nov. 2026) — séparé des archives v6.0–v6.2.

**Archives :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)  
**Ce dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)

---

## État au 19 novembre 2026 (soir)

### Matrice
```bash
python scripts/restore_tcga_enriched_p2.py
# → data/tcga_enriched_p2.csv  (179×24, SHA 6a53c8c6…)
```
Pureté InfiniumPurify jointe (n=178).

### Signaux après contrôle pureté (P2.7–P2.8)
| Signal | Après pureté | Statut |
|--------|--------------|--------|
| KRAS → CEA | atténué (p≈0,07–0,12) · haut quartile p=0,033 | **faible résiduel** |
| KRAS → CA125 | atténué | faible |
| MTAP → CEA / CA125 | **disparu** | confondu par pureté |

### Avancement
- [x] Dépôt + plan + protocoles
- [x] Matrice enrichie Firehose + restore fonctionnel
- [x] Tests directs + residualisation KRAS
- [x] Contrôle pureté (InfiniumPurify) — négatifs honnêtes documentés
- [ ] UNIVERSAL_LOG v6.2 avec pureté covariable
- [ ] ESTIMATE / ABSOLUTE en complément
- [ ] Validation externe GEO

### Structure clé
```
├── livre-blanc/livre-blanc-phase2.md   ← P2.8 à jour
├── results/P2_006_purity_confounding.md
├── results/P2_007_kras_after_purity.md
├── data/b64_chunks/                    ← payload matrice
└── scripts/restore_tcga_enriched_p2.py
```

Travail bénévole, non clinique, données publiques. Aucune promesse thérapeutique.
