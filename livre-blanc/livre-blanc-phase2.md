# Livre blanc — PDAC Phase 2

**Document vivant** — mis à jour à chaque étape.  
**Dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)  
**Archives :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)

---

## P2.0 — Pourquoi un nouveau dépôt

Date : 19 novembre 2026. Séparation archives (v6.0–v6.2, §1–§8.42) / phase 2 (recentrage signaux robustes).

---

## P2.1 — Plan d’attaque et critères de rétention

Priorités : (1) stratification CA125/CEA, (2) contexte MTAP/PRMT5, (3) ATR surveillance.  
Rétention = nul permuté + rotation + ≥1 couche orthogonale.

---

## P2.2 — Inventaire des axes

Axes actionnables : VAF/expression KRAS, statut MTAP (GISTIC −2), pureté ESTIMATE.

---

## P2.3 — Matrice enrichie construite

Date : 19 novembre 2026.

- Téléchargement Firehose PAAD RSEM (MD5 `b09569ce…` ✓) + GISTIC (MD5 `816034f7…` ✓)
- `data/tcga_enriched_p2.csv` : **179 × 23**, SHA256 `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`
- MTAP-del : 43/177 | kras_fort : 12
- Gènes : MUC16, CEACAM5, KRAS, panel contexte, PRMT5, MTAP, CDKN2A
- Provenance : `provenance/PROVENANCE_tcga_enriched_p2.md`

---

## P2.4 — P2-PROTO-001 lite (tests directs)

Date : 19 novembre 2026. Sans pipeline v6.2 (tests non paramétriques + Spearman).

### Confirmé

| Association | Stat | p |
|-------------|------|---|
| KRAS ↔ MUC16 (Spearman) | ρ=0,279 | 1,6×10⁻⁴ |
| KRAS ↔ CEACAM5 (Spearman) | ρ=0,342 | 2,8×10⁻⁶ |
| kras_fort (top-12) → MUC16 ↑ | Δmed +1,95 | 0,014 |
| kras_fort (top-12) → CEACAM5 ↑ | Δmed +2,59 | 0,006 |

### Nouveau signal exploratoire

| Association | Stat | p |
|-------------|------|---|
| MTAP-del → MUC16 ↑ | Δmed +1,85 | 0,011 |
| MTAP-del → CEACAM5 ↑ | Δmed +1,48 | 0,004 |

Fisher kras_fort × MTAP-del : OR=3,46, p=0,073 (identique archives).

### Verdict lite

Signal CA125/CEA chez KRAS élevé **retenu au niveau expression**.  
Lien MTAP–MUC16/CEACAM5 **exploratoire** — à soumettre aux critères stricts (nul, rotation, pureté, v6.2).

Détail : `results/P2_001_lite_verdict.md`, `results/p2_proto001_lite_direct_tests.csv`.

---

## Journal phase 2

| Date | Action | Note |
|------|--------|------|
| 19 nov 2026 | Création dépôt phase 2 | Séparation archives |
| 19 nov 2026 | P2.1–P2.2 + PROTO-001/002 | Plan + inventaire + protocoles |
| 19 nov 2026 | P2.3 matrice enrichie | Firehose re-téléchargé, SHA 6a53c8c6 |
| 19 nov 2026 | P2.4 tests directs lite | Signal CA125/CEA confirmé ; MTAP exploratoire |

---

*Suite : pureté ESTIMATE, runs v6.2, validation externe.*
