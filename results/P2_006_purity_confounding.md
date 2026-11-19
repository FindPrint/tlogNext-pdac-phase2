# P2.6 — Pureté tumorale et confounding (19 nov 2026)

**Source pureté :** InfiniumPurify (Zenodo record 253193, fichier PAAD.txt)  
**Matrice :** `tcga_enriched_p2.csv` + jointure sur barcode 15 caractères  
**n avec pureté :** 178 / 179

## Corrélations pureté

| Variable | Spearman ρ | p |
|----------|------------|---|
| ceacam5_rank | **+0,53** | 3×10⁻¹⁴ |
| kras_rank | **+0,47** | 3×10⁻¹¹ |
| muc16_rank | +0,24 | 0,001 |
| mtap_del | +0,27 | 3×10⁻⁴ |

La pureté est fortement associée aux ranks CEA et KRAS.

## Tests de confounding

| Test | Résultat |
|------|----------|
| resid_cea ~ pureté, puis ~ mtap_del | r=0,067 · **p=0,37** (ns) |
| MW resid_cea (mtap_del) | **p=0,37** (ns) |
| double résidu (KRAS + pureté) ~ mtap_del | r=0,074 · **p=0,33** (ns) |

## Verdict honnête

Le signal **MTAP-del → CEACAM5/CEA** observé en P2.4–P2.5 **ne survit pas** au contrôle de pureté tumorale (InfiniumPurify).

- Après residualisation pureté (seule ou + KRAS), l’association devient non significative.
- La pureté explique une grande part de la variance de CEA rank (ρ≈0,53).
- Le signal KRAS ↔ CEA reste à re-tester après contrôle pureté (priorité suivante).

## Implications

1. Les associations MTAP→sécrétoire (CEA/CA125) dans TCGA-PAAD sont **probablement confondues** par la pureté / teneur stromale.
2. Tout run UNIVERSAL_LOG v6.2 doit inclure pureté (ou ESTIMATE/ABSOLUTE) comme covariable ou filtre.
3. Source pureté à citer : Zenodo 253193 (InfiniumPurify). ESTIMATE MD Anderson reste souhaitable en complément.

## Fichiers
- `data/purity_infiniumpurify_paad.txt` (partiel sur repo ; source complète Zenodo)
- Matrice enrichie + pureté générée localement : `tcga_enriched_p2_with_purity.csv`

*Travail exploratoire, non clinique.*
