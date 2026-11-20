# P2.14 — Analyse des résultats (run full partiel + runner safe)

## 1. Ce qui a été produit

### A. Runner safe (complet, checkpointé)
`pipeline_runs/pdac_kras_cea/`

| Métrique | Valeur |
|----------|--------|
| Cohen d (kras_high vs cea_resid) | **+0,344** |
| null_p (2000 perms) | **0,047** |
| retained | **True** |
| Contrôle négatif mtap_del null_p | 0,243 (pass) |

### B. Pipeline full v6.2.0 (partiel — interrompu après paysage)
`pipeline_runs/v6_full_pdac/`

| Étape | Statut |
|-------|--------|
| MC harmonique guidé | ✓ score 0,450 · w_size=30 · min_grp=6 |
| T0 détecté | ✓ **44,61 %** → kras_rank ≈ **79** (spread 77–81) |
| Paysage 29 estimateurs | ✓ PNG générés |
| Tension holographique | ✓ divergence dominante (Δ=3,857) |
| Cascades L1–L7 / JSON final | ✗ non terminé (kill environnement) |

---

## 2. Analyse du T0 (pipeline full)

Le pipeline place un seuil T0 à **kras_rank ≈ 79** (≈44,6 % de la progression ordonnée).

### Test pre vs post T0 sur `cea_resid_purity`

| Groupe | n | mean cea_resid |
|--------|---|----------------|
| pre T0 (rank < 79) | 78 | −0,52 |
| post T0 (rank ≥ 79) | 100 | +0,40 |

- Mann-Whitney p = **0,80**
- Cohen d = **0,021** (négligeable)

**Verdict T0 :** le seuil de complexité détecté par v6 **ne sépare pas** l’expression CEA résidualisée. Ce n’est **pas** le support du signal biologique retenu.

---

## 3. Signal réellement retenu = effet de queue (Q4)

| Groupe | n | mean cea_resid | median |
|--------|---|----------------|--------|
| kras_high = 0 | 133 | −3,71 | −4,57 |
| kras_high = 1 (Q4) | 45 | **+10,97** | **+18,02** |

- Cohen d = +0,34
- null_p = 0,047
- GEO (sans pureté) : d = 0,52–0,68 · null_p < 0,02

→ Signal de **haut quartile**, pas de transition au milieu de série.

---

## 4. Lecture des figures v6

### Paysage de complexité (29 estimateurs)
- Ligne rouge verticale = T0 (~45 %)
- Nombreux estimateurs en régime **saturation** (Higuchi, Petrosian, Sevcik, BoxCounting…)
- Classe **criticality** (CorrelationD2, Grassberger, TwoNN, DANCo, Fisher) : fluctuations sans rupture nette alignée sur CEA
- Classe **divergence** (LevinaBickel, PCA, PersistentHomology…) : dominante dans la tension holographique

### Tension holographique v5.2
- **divergence** médiane géométrique la plus haute (≈5,5) · Δ = 3,857 vs autres classes
- z-croisé des médianes : divergence >> saturation / criticality / null_reference
- Interprétation : le paysage est tiré par des estimateurs de divergence de dimension, **pas** par une transition nette de l’observable CEA au T0

### Warning skew
`Precision loss in moment calculation` — certaines fenêtres ont variance quasi nulle (séries plates / ranks). Attendu sur n=178 avec w_size=30 ; ne invalide pas T0 mais limite certains estimateurs d’ordre supérieur.

---

## 5. Synthèse intégrée

| Question | Réponse |
|----------|--------|
| Le full v6 a-t-il tourné ? | Partiellement (jusqu’au paysage + T0) |
| T0 est-il le signal CEA ? | **Non** (d≈0, pre/post ns) |
| Quel signal reste ? | **kras_high (Q4) → CEA résidualisé pureté** |
| Rétention nuls | null_p=0,047 · retained |
| Validation GEO | Oui (GSE71729, GSE62452) |
| MTAP | Non retenu (confondu pureté) |

### Implications pour la suite
1. Le T0 v6 décrit une structure de **complexité des estimateurs** le long de kras_rank, pas l’effet CEA.
2. Pour capturer le signal Q4 dans v6, il faudrait un contraste explicite haut/bas quartile (ou un contrôle binaire `kras_high`) plutôt qu’une progression continue seule.
3. Le runner safe reste la référence de rétention pour cet axe dans cet environnement.
4. Relancer le full v6 chez toi jusqu’au JSON final reste utile pour L1–L7, mais le verdict biologique principal ne changera probablement pas sur le T0 continuum.

---

## Fichiers
- Safe : `pipeline_runs/pdac_kras_cea/SUMMARY.json`
- Full partiel : `pipeline_runs/v6_full_pdac/*.png` + logs
- Input : `data/pdac_v6_input.csv`

*Analyse au 19 nov 2026 — reprise après interruption du full run.*
