# Résumé MTAP (données importées) — 19 novembre 2026

Source : `data/mtap_gistic_status.csv` (archives).

## Effectifs

- Lignes totales : 178
- Avec GISTIC non manquant : 177 (TCGA-FB-A4P6 exclu)
- **MTAP-del (GISTIC −2)** : compter dans le fichier
- **kras_fort = True** : 12 tumeurs (les plus fortes expression KRAS, convention archives)

## Lien KRAS-fort × MTAP-del (rappel archives §8.26 / §8.40)

- Fisher déjà calculé : OR ≈ 3,46, p ≈ 0,073 (non significatif au seuil habituel)
- Ne pas retraiter comme un nouveau résultat ; c’est le contexte de P2-PROTO-002.

## Usage phase 2

- Colonne `mtap_del` dérivable pour stratification / axe binaire.
- Colonne `kras_fort` déjà présente pour analyses ciblées sur le groupe KRAS élevé.
