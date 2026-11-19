# Livre blanc — PDAC Phase 2

**Document vivant.**  
**Dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)  
**Archives :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)

---

## P2.0 — Nouveau dépôt (19 nov. 2026)

Séparation archives / phase 2. Recentrage sur signaux robustes + axes légitimes + critères stricts.

---

## P2.1 — Plan et critères de rétention

Priorités : CA125/CEA stratification → contexte MTAP/PRMT5 → ATR surveillance.  
Rétention = nul + rotation + ≥1 orthogonalité.

---

## P2.2 — Inventaire axes

VAF/expression KRAS, MTAP (GISTIC −2), pureté ESTIMATE (à ajouter).

---

## P2.3 — Matrice enrichie

- Firehose RSEM + GISTIC re-téléchargés (MD5 vérifiés)
- `tcga_enriched_p2.csv` : 179×23, SHA256 `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`
- MTAP-del 43/177 · kras_fort 12
- Restauration : `python scripts/restore_tcga_enriched_p2.py` (si payload b64 présent)

---

## P2.4 — Tests directs lite (confirmés)

| Association | Stat | p |
|-------------|------|---|
| KRAS ↔ MUC16 | ρ=0,28 | 1,6×10⁻⁴ |
| KRAS ↔ CEACAM5 | ρ=0,34 | 2,8×10⁻⁶ |
| kras_fort → MUC16/CEA ↑ | Δmed +1,9 / +2,6 | 0,014 / 0,006 |
| MTAP-del → MUC16/CEA ↑ | Δmed +1,9 / +1,5 | 0,011 / 0,004 |

---

## P2.5 — Analyses étendues MTAP (contrôle KRAS)

| Test | Cible | Résultat |
|------|-------|----------|
| Résidus ~ KRAS | CEACAM5 | Δmed +1,46 **p=0,020** |
| Résidus ~ KRAS | MUC16 | Δmed +1,19 p=0,063 |
| Spearman GISTIC | CEACAM5 | ρ=−0,33 **p=7×10⁻⁶** |
| Spearman GISTIC | MUC16 | ρ=−0,25 **p=9,5×10⁻⁴** |
| Cohen d MTAP-del | CEACAM5 / MUC16 | +0,52 / +0,35 |

**Verdict intermédiaire :**  
- Signal KRAS→CA125/CEA **solide**.  
- Signal MTAP→CEACAM5 **exploratoire mais résistant** à l’ajustement KRAS.  
- MTAP→MUC16 plus fragile.

Détail : `results/P2_001_extended_verdict.md`.

---

## Journal

| Date | Action |
|------|--------|
| 19 nov | Dépôt phase 2 + protocoles |
| 19 nov | Matrice Firehose + tests lite |
| 19 nov | Analyses étendues MTAP (résidus, ordinal, d) |

*Suite : pureté ESTIMATE, pipeline v6.2, validation GEO.*
