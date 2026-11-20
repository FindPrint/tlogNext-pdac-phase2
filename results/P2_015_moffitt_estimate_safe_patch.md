# P2.15 — A Moffitt · C ESTIMATE · D patch safe

## A. Moffitt × kras_high × CEA (GSE71729)

Proxy Moffitt (marqueurs publics) sur 145 primaires :
- **Basal** : mean(KRT5, KRT17, S100A2, KRT6A)
- **Classical** : mean(GATA6, HNF4A, TFF1, LGALS4)
- Label = basal si (basal − classical) > médiane, sinon classical → 72 / 73

| Sous-type | n kras_high | Cohen d (→ CEA) | MW p | null_p (2000) |
|-----------|-------------|-----------------|------|---------------|
| **classical** | 16 | **+0,61** | 0,041 | **0,045** |
| basal | 20 | +0,47 | 0,127 | 0,072 |

Spearman KRAS–CEA : classical ρ=0,33 (p=0,004) · basal ρ=0,21 (p=0,084)

**Lecture :** l’effet kras_high→CEA est **présent dans les deux**, plus net et retenu sous nuls dans **classical**. Ce n’est pas exclusif à basal.

Fichier : `data/geo/GSE71729_primary_moffitt_proxy.csv`  
*Proxy = score marqueurs, pas les labels officiels Moffitt 2015 (suppl. non récupéré ici).*

---

## C. Pureté ESTIMATE

Tentatives :
- MD Anderson ESTIMATE tables → HTML (pas de dump direct)
- Aran *Nat Commun* 2015 ESM xlsx → paywall / fichier invalide
- Zenodo TCGA_tumor_purity → **InfiniumPurify** (déjà utilisé), pas ESTIMATE

**Statut :** ESTIMATE non joint dans cette session.  
Pureté de référence reste **InfiniumPurify** (n=178).  
À faire hors ligne : table Aran (ESTIMATE / CPE / ABSOLUTE) jointe sur `bcr_patient_barcode`.

---

## D. Patch safe pour le vrai v6.2

Notes livrées : `scripts/v6_safe_patch_notes.md`

Idée minimale :
1. `checkpoints/01_mc_opt.json` après MC
2. `checkpoints/02_t0.json` après T0
3. `checkpoints/03_landscape_done.json` après PNG estimateurs
4. CLI `--resume` qui saute les stages OK

Prototype validé : `scripts/run_v6_safe.py`  
Le full `universal_v6.2.0_cohen.py` n’a **pas** encore été modifié ligne à ligne (trop gros pour un patch unique ici) ; les notes indiquent où brancher.

---

## Synthèse A+C+D

| Item | Résultat |
|------|----------|
| Moffitt × Q4 | Effet plus clair en **classical** (null_p=0,045) |
| ESTIMATE | Non obtenu cette session |
| Safe v6 | Spec + prototype ; intégration full = prochaine étape code |
