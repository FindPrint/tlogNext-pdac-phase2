# Livre blanc — PDAC Phase 2

**Document vivant.**  
**Dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)  
**Archives :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)

---

## P2.0 — Nouveau dépôt (19 nov. 2026)
Séparation archives / phase 2. Critères stricts (nul + rotation + orthogonalité).

---

## P2.3 — Matrice enrichie
- `tcga_enriched_p2.csv` · 179×24 · SHA256 `6a53c8c6…`
- Restauration : `python scripts/restore_tcga_enriched_p2.py` (**fonctionne**)
- Pureté InfiniumPurify jointe (n=178)

---

## P2.4–P2.6 — Signaux bruts
- KRAS ↔ CEA ρ=0,34 · CA125 ρ=0,28
- MTAP-del → CEA Cohen d=+0,53 · CA125 +0,46
- Résiste au contrôle KRAS seul

---

## P2.7 — Pureté confond MTAP→CEA
Après residualisation pureté (InfiniumPurify) :
- MTAP → CEA **p ≈ 0,33–0,37 (ns)**
→ Signal MTAP→sécrétoire **largement confondu** par pureté.
Détail : `results/P2_006_purity_confounding.md`

---

## P2.8 — KRAS après contrôle pureté (19 nov 2026)

| Axis | Modèle | ρ | p |
|------|--------|---|---|
| CEA | brut | 0,343 | 2,7×10⁻⁶ |
| CEA | ~ pureté puis ~ KRAS | 0,138 | **0,067** |
| CEA | les deux résidualisés | 0,116 | 0,122 |
| CA125 | ~ pureté puis ~ KRAS | 0,166 | **0,027** |
| CA125 | les deux résidualisés | 0,143 | 0,057 |

**kras_high (Q4) vs CEA résidualisé pureté** : MW p=0,033 · Cohen d≈0,34

### Verdict mis à jour
- Le signal **KRAS → CEA** est **fortement atténué** par pureté (passe de très significatif à borderline/ns selon le modèle).
- Un effet résiduel du **haut quartile KRAS** persiste (p=0,033).
- CA125 un peu plus résistant.
- Interprétation : une partie du lien KRAS–sécrétoire est indépendante de la pureté, mais l’effet global était surestimé sans contrôle pureté.

Détail : `results/P2_007_kras_after_purity.md`

---

## Synthèse des signaux (état au 19 nov soir)

| Signal | Brut | Après pureté | Statut |
|--------|------|--------------|--------|
| KRAS → CEA | fort | atténué / borderline | **faible mais non nul** |
| KRAS → CA125 | moyen | atténué | faible |
| MTAP → CEA | moyen | **disparu** | confondu |
| MTAP → CA125 | moyen | disparu | confondu |

---

## Prochaines étapes (P2.9+)
1. **UNIVERSAL_LOG v6.2** avec pureté comme covariable / filtre (nuls + rotations sur axes prioritaires).
2. Compléter pureté avec ESTIMATE ou ABSOLUTE si disponible.
3. Validation externe GEO (GSE71729 / GSE62452) en contrôlant pureté approximative si possible.
4. Interaction formelle KRAS × pureté.

---

## Journal

| Date | Action |
|------|--------|
| 19 nov | Dépôt + matrice + tests lite |
| 19 nov | Residualisation KRAS + stratification |
| 19 nov soir | P2.7 pureté confond MTAP |
| 19 nov soir | **P2.8 KRAS atténué mais résidu haut quartile** |

*Travail bénévole, non clinique, données publiques. Aucune promesse thérapeutique.*
