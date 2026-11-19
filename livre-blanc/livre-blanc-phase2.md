# Livre blanc — PDAC Phase 2

**Document vivant.**  
**Dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)  
**Archives :** [FindPrint/tlogNext-cancer-pdac](https://github.com/FindPrint/tlogNext-cancer-pdac)

---

## P2.0 — Cadre
Nouveau dépôt phase 2 (19 nov 2026). Critères de rétention : null + rotation + orthogonalité. Séparé des archives v6.

---

## P2.3 — Matrice
- `tcga_enriched_p2.csv` · 179×24 · SHA256 `6a53c8c6…`
- Restauration : `python scripts/restore_tcga_enriched_p2.py` (**OK**)
- Pureté InfiniumPurify jointe (n=178)

---

## P2.4–P2.6 — Signaux bruts (sans pureté)
KRAS ↔ CEA ρ=0,34 · MTAP-del → CEA d=+0,53. Résistent au contrôle KRAS seul.

---

## P2.7 — Pureté confond MTAP
Après residualisation pureté : MTAP → CEA **ns** (p≈0,33–0,37).  
→ Signal MTAP **non retenu**.

---

## P2.8 — KRAS après pureté
KRAS continu → CEA : ρ chute à ~0,12 (p≈0,07–0,12).  
kras_high (Q4) vs CEA résidualisé : p=0,033 · d≈0,34.

---

## P2.9 — Tests de rétention (nuls, 2000 perms) — 19 nov soir

| Test | Stat | null_p | Décision |
|------|------|--------|----------|
| kras_r vs cea_r | ρ=+0,12 | 0,13 | **DROP** |
| kras_r vs ca125_r | ρ=+0,14 | 0,056 | borderline / DROP |
| **kras_high vs cea_r** | d=+0,34 | **0,054** | **faible RETAIN** |
| mtap_del vs cea_r | d=+0,20 | 0,26 | DROP (contrôle OK) |

### Synthèse finale des signaux

| Signal | Après pureté + nuls | Statut final |
|--------|---------------------|--------------|
| MTAP → CEA/CA125 | disparu | **Non retenu** |
| KRAS continu → CEA | null_p > 0,10 | **Non retenu** |
| kras_high → CEA résidualisé | null_p ≈ 0,054 | **Faible / hypothétique** |

Un seul signal frôle le seuil de rétention : le haut quartile d’expression KRAS reste faiblement associé à CEA après contrôle pureté. Effet petit, à confirmer en externe.

Détail : `results/P2_009_retention_nulls.md`

---

## Prochaines étapes
1. Validation externe (GEO GSE71729 / GSE62452) du signal kras_high → CEA (même avec pureté approximative).
2. Run UNIVERSAL_LOG v6.2 full sur cet axe unique restant (avec pureté covariable).
3. Compléter pureté (ESTIMATE/ABSOLUTE) si disponible.
4. Documenter formellement les négatifs (MTAP, KRAS continu).

---

## Journal

| Date | Action |
|------|--------|
| 19 nov | Dépôt + matrice + tests lite |
| 19 nov | Residualisation + pureté |
| 19 nov soir | P2.7–P2.8 : MTAP confondu, KRAS atténué |
| 19 nov soir | **P2.9 rétention nuls : seul kras_high faible** |

*Travail bénévole, non clinique, données publiques. Aucune promesse thérapeutique.*
