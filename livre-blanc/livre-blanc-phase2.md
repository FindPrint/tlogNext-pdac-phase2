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
- `tcga_enriched_p2.csv` : 179×24, SHA256 `6a53c8c64a20f8da0464642308841a3afafeade41bf044e0de226116fa7bfcfd`
- MTAP-del 43/179 · kras_fort (top quartile) ~45
- Restauration : `python scripts/restore_tcga_enriched_p2.py` (chunks b64)
- **Note data 19 nov soir :** chunk_04 a nécessité une correction (1 caractère). Reconstruction depuis GitHub en cours de stabilisation. Matrice locale = source de vérité.

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

Détail : `results/P2_001_mtap_context_verdict.md`.

---

## P2.6 — Analyses prioritaires + stratification (19 nov 2026 soir)

### Spearman (ranks)
- kras_rank ↔ muc16_rank : ρ = 0,279 · p = 1,6×10⁻⁴
- kras_rank ↔ ceacam5_rank : ρ = 0,342 · p = 2,8×10⁻⁶
- muc16_rank ↔ ceacam5_rank : ρ = 0,224 · p = 2,6×10⁻³

### Effets MTAP-del (n_del = 43)
| Axis | Cohen d | MW p |
|------|---------|------|
| ceacam5_rank | **+0,527** | 0,0033 |
| muc16_rank | **+0,456** | 0,010 |
| CEACAM5_log2 | +0,523 | 0,0033 |
| MUC16_log2 | +0,352 | 0,010 |
| kras_rank | +0,264 | 0,13 (ns) |
| PRMT5_log2 | −0,023 | 0,83 (ns) |
| MTAP_log2 | **−1,49** | 2,5×10⁻¹² |
| CDKN2A_log2 | **−1,46** | 7×10⁻¹⁴ |

### Residualisation KRAS rank
- resid_muc16_rank ~ mtap_del : r = 0,169 · p = 0,023
- resid_ceacam5_rank ~ mtap_del : r = 0,190 · p = 0,011

→ Les deux signaux MTAP survivent au contrôle de KRAS rank.

### Stratification kras_high (quartile supérieur)
- kras_high=False (n_wt=106, n_del=28) : MW ceacam5_rank p = 0,0099
- kras_high=True (n_wt=30, n_del=15) : MW ceacam5_rank p = 0,60 (ns)

→ L’effet MTAP→CEA est plus clair hors du haut quartile KRAS (puissance limitée dans le stratum élevé).

### Statut pureté ESTIMATE
Non encore intégré. À récupérer depuis Firehose ESTIMATE ou ABSOLUTE scores pour contrôle de confounding pureté/stroma.

### Prochaines étapes P2.7+
1. Fix final data payload (chunk_04 ou upload CSV complet 58 ko).
2. Intégrer pureté ESTIMATE.
3. Lancer UNIVERSAL_LOG v6.2 full (nuls + rotations) sur axes prioritaires : kras_rank, muc16_rank, ceacam5_rank, mtap_del.
4. Validation externe GEO GSE71729 / GSE62452.
5. Interaction formelle KRAS × MTAP.

---

## Journal

| Date | Action |
|------|--------|
| 19 nov | Dépôt phase 2 + protocoles |
| 19 nov | Matrice Firehose + tests lite |
| 19 nov | Analyses étendues MTAP (résidus, ordinal, d) |
| 19 nov soir | P2.6 : residualisation confirmée, stratification KRAS, mise à jour livre blanc |

*Suite : pureté ESTIMATE, pipeline v6.2 full, validation GEO.*
