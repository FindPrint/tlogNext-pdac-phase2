# Livre blanc — PDAC Phase 2

**Document vivant.**  
**Dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)

---

## Synthèse exécutive (19 nov 2026)

Après contrôle pureté + tests de rétention (nuls) dans TCGA-PAAD, un seul signal frôle le seuil : **kras_high (Q4 expression) → CEA plus élevé** (d≈0,34 · null_p≈0,054).

**Validation externe GEO :**
- **GSE71729** (n=145 primary) : d=+0,52 · null_p=0,008
- **GSE62452** (n=69 tumor) : d=+0,68 · null_p=0,019

→ Le signal se **réplique** dans deux cohortes indépendantes avec des effets moyens à forts.

Les signaux MTAP→CEA et KRAS continu→CEA ne sont **pas retenus** après pureté.

---

## P2.3 — Matrice TCGA
`tcga_enriched_p2.csv` · 179×24 · SHA256 `6a53c8c6…`  
Restauration : `python scripts/restore_tcga_enriched_p2.py`  
Pureté InfiniumPurify jointe (n=178).

---

## P2.7–P2.9 — Contrôle pureté + rétention
- MTAP → CEA : confondu par pureté → **DROP**
- KRAS continu → CEA après pureté : null_p > 0,10 → **DROP**
- kras_high → CEA résidualisé : null_p ≈ 0,054 → **faible RETAIN**

---

## P2.10 — Validation GEO (19 nov soir)

| Dataset | n | ρ KRAS–CEA | d kras_high | null_p |
|---------|---|------------|-------------|--------|
| TCGA (après pureté) | 178 | ~0,12 | 0,34 | 0,054 |
| GSE71729 | 145 | 0,27 | **0,52** | **0,008** |
| GSE62452 | 69 | 0,44 | **0,68** | **0,019** |

Détail : `results/P2_010_GEO_validation.md`

---

## Statut des axes

| Axe | TCGA + pureté + nuls | GEO | Décision |
|-----|----------------------|-----|----------|
| MTAP → CEA/CA125 | DROP | — | Non retenu |
| KRAS continu → CEA | DROP | — | Non retenu |
| **kras_high → CEA** | faible RETAIN | **répliqué** | **Retenu pour suivi** |

---

## Prochaines étapes
1. Run UNIVERSAL_LOG v6.2 **ciblé** sur kras_high / CEA (avec pureté covariable) dans TCGA.
2. Explorer si le signal kras_high→CEA est lié au sous-type basal/classical (Moffitt) dans GSE71729.
3. Compléter pureté (ESTIMATE) si possible.

---

## Journal

| Date | Action |
|------|--------|
| 19 nov | Matrice + pureté + rétention nuls |
| 19 nov soir | **P2.10 validation GEO positive (GSE71729 + GSE62452)** |

*Travail bénévole, non clinique, données publiques. Aucune promesse thérapeutique.*
