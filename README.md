# PDAC Phase 2 — Recentrage et pistes prioritaires

**Dépôt phase 2** (19 nov. 2026) — séparé des archives v6.0–v6.2.

**Archives :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)  
**Ce dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)

---

## État final de la session (19 nov 2026 soir)

### Matrice
```bash
python scripts/restore_tcga_enriched_p2.py
# → 179×24 · SHA256 6a53c8c6…
```
Pureté InfiniumPurify jointe (n=178).

### Signaux après pureté + tests de rétention (nuls)

| Signal | null_p | Statut |
|--------|--------|--------|
| MTAP → CEA/CA125 | > 0,25 | **Non retenu** (confondu pureté) |
| KRAS continu → CEA | 0,13 | **Non retenu** |
| **kras_high (Q4) → CEA résidualisé** | **0,054** | **Faible / hypothétique** |

Un seul axe frôle le seuil de rétention. Effet petit (d≈0,34).

### Documents
- Livre blanc : `livre-blanc/livre-blanc-phase2.md` (P2.9)
- `results/P2_006_purity_confounding.md`
- `results/P2_007_kras_after_purity.md`
- `results/P2_009_retention_nulls.md`

### Avancement
- [x] Matrice enrichie + restore fonctionnel
- [x] Contrôle pureté (InfiniumPurify)
- [x] Tests de rétention (nuls) sur axes prioritaires
- [x] Négatifs honnêtes documentés (MTAP, KRAS continu)
- [ ] Validation externe GEO du signal kras_high
- [ ] UNIVERSAL_LOG v6.2 full sur l’axe restant
- [ ] ESTIMATE / ABSOLUTE en complément

Travail bénévole, non clinique, données publiques. Aucune promesse thérapeutique.
