# Livre blanc — PDAC Phase 2

**Document vivant.**  
**Dépôt :** [FindPrint/tlogNext-pdac-phase2](https://github.com/FindPrint/tlogNext-pdac-phase2)

---

## Synthèse exécutive

**Signal retenu :** kras_high (Q4 expression KRAS) → CEA plus élevé, après contrôle pureté.

| Source | d | null_p |
|--------|---|--------|
| TCGA + pureté (safe runner) | +0,34 | 0,047 |
| GSE71729 | +0,52 | 0,008 |
| GSE62452 | +0,68 | 0,019 |

MTAP→CEA et KRAS continu→CEA : **non retenus** (pureté).

---

## P2.14 — Analyse run full v6.2 (partiel) + safe (19–20 nov)

### Full UNIVERSAL_LOG v6.2.0 (mode fast)
- MC harmonique ✓ · T0 = **44,6 %** → kras_rank ≈ **79**
- Paysage 29 estimateurs ✓ · tension holographique : **divergence** dominante (Δ=3,86)
- Cascades L1–L7 : non terminées (interruption environnement)

### T0 vs signal CEA
Pre vs post T0 sur `cea_resid_purity` : **d ≈ 0,02 · p ≈ 0,80**

→ Le T0 de complexité **n’est pas** le support du signal CEA.  
→ Le signal retenu est un **effet de queue (Q4)**, pas une transition au milieu de série.

### Runner safe (complet)
Cohen d = +0,34 · null_p = 0,047 · retained · contrôle mtap_del OK.

Détail : `results/P2_014_analysis_partial_v6_and_safe.md`

---

## Historique court

| Étape | Résultat |
|-------|----------|
| P2.7 | Pureté confond MTAP |
| P2.8–9 | KRAS continu atténué ; Q4 frôle rétention |
| P2.10 | GEO valide Q4→CEA |
| P2.12–13 | Runner safe + lancement full v6 |
| **P2.14** | **T0 ≠ signal CEA ; Q4 confirmé** |

---

## Suite possible
1. Finir le full v6 chez toi (JSON L1–L7) pour documentation complète.
2. Contraste explicite binaire `kras_high` dans v6 (plutôt que progression seule).
3. Sous-types Moffitt dans GSE71729 vs kras_high.

*Travail bénévole, non clinique, données publiques.*
