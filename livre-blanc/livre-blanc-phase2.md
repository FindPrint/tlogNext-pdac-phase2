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

VAF/expression KRAS, MTAP (GISTIC −2), pureté (InfiniumPurify intégré ; ESTIMATE encore souhaitable).

---

## P2.3 — Matrice enrichie

- Firehose RSEM + GISTIC re-téléchargés (MD5 vérifiés)
- `tcga_enriched_p2.csv` : 179×24, SHA256 `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`
- **Restauration OK** : `python scripts/restore_tcga_enriched_p2.py` (chunks b64 vérifiés)
- MTAP-del 43/179

---

## P2.4 — Tests directs lite

| Association | Stat | p |
|-------------|------|---|
| KRAS ↔ MUC16 | ρ=0,28 | 1,6×10⁻⁴ |
| KRAS ↔ CEACAM5 | ρ=0,34 | 2,8×10⁻⁶ |
| MTAP-del → MUC16/CEA ↑ | Δmed +1,9 / +1,5 | 0,011 / 0,004 |

---

## P2.5 — Analyses étendues MTAP (contrôle KRAS)

Signal MTAP→CEACAM5 résistant à l’ajustement KRAS (p≈0,01–0,02).  
Détail : `results/P2_001_mtap_context_verdict.md`.

---

## P2.6 — Analyses prioritaires + stratification

Cohen d MTAP-del : CEA +0,53 · CA125 +0,46.  
Résidus KRAS survivent. Stratification : effet plus clair hors haut quartile KRAS.

---

## P2.7 — Pureté tumorale = confounding majeur (19 nov 2026)

**Source :** InfiniumPurify (Zenodo 253193), n=178 matchés.

| Variable | ρ vs pureté | p |
|----------|-------------|---|
| ceacam5_rank | **+0,53** | 3×10⁻¹⁴ |
| kras_rank | **+0,47** | 3×10⁻¹¹ |
| muc16_rank | +0,24 | 0,001 |
| mtap_del | +0,27 | 3×10⁻⁴ |

**Après residualisation pureté (seule ou + KRAS) :**
- MTAP-del → CEA : **p ≈ 0,33–0,37 (ns)**

### Verdict mis à jour
Le signal **MTAP → CEA/CA125** observé précédemment est **largement confondu par la pureté tumorale**. Il ne passe pas le contrôle pureté.

Conséquences :
1. Tout futur run (UNIVERSAL_LOG ou tests directs) doit inclure pureté comme covariable/filtre.
2. Le signal KRAS ↔ CEA doit être re-testé après contrôle pureté (prochaine priorité).
3. Négatif honnête documenté : `results/P2_006_purity_confounding.md`.

---

## Prochaines étapes (P2.8+)
1. Re-tester KRAS → CEA/CA125 après contrôle pureté.
2. Intégrer ESTIMATE / ABSOLUTE en complément d’InfiniumPurify.
3. Lancer UNIVERSAL_LOG v6.2 avec pureté dans le modèle (nuls + rotations).
4. Validation externe GEO.

---

## Journal

| Date | Action |
|------|--------|
| 19 nov | Dépôt phase 2 + protocoles + matrice |
| 19 nov | Tests lite + residualisation KRAS |
| 19 nov soir | P2.6 analyses prioritaires |
| 19 nov soir | **P2.7 pureté : signal MTAP→CEA confondu** |

*Travail bénévole, non clinique, données publiques. Aucune promesse thérapeutique.*
