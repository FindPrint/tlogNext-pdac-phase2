# P2.17 — Run full v6 contrôle binaire `kras_high`

**Sortie :** `pipeline_runs/v6_kras_high/`  
**Statut :** `✓ Pipeline Master completed successfully!`

```bash
--control kras_high --target cea_resid_purity --mode fast --domain biology --seed 42
```

## Comparaison des deux runs full

| Métrique | control=`kras_rank` | control=`kras_high` |
|----------|---------------------|---------------------|
| T0 % | 44,6 % | 44,6 % |
| T0 valeur contrôle | rank ≈ 79 | **0** (encore dans le bas) |
| Passage à 1 (high) | — | seuils T+1/T+2 ≈ 77 % |
| L1 direction | down | down |
| L1 conf / Δrel | 0,57 / −0,47 | 0,57 / −0,49 |
| L3 | post · cross 0,90 | post · cross 0,90 |
| L4 | high ~0,72 | high ~0,71 |
| L7a désaccord | oui | oui |
| L7b | **FRAGILE** | **FRAGILE** |
| WF t0_std | 24,1 | **15,2** (mieux, encore FAIL) |
| Holo Δ | 3,86 | 3,08 |
| Régime | divergence | divergence |

## Lecture

1. Passer en contrôle binaire **ne résout pas** le désaccord L1↓ vs L3↑ ni le verdict L7b FRAGILE.
2. Le T0 % reste ~45 % car l’axe de progression interne du pipeline n’est pas recalibré uniquement sur le saut 0→1 ; en valeur brute, T0 tombe encore dans `kras_high=0`, et le passage à 1 est plutôt vers **T+1 (~77 %)**, cohérent avec Q4 en fin de série ordonnée par rank.
3. Walk-forward un peu **plus stable** (t0_std 15 vs 24) mais toujours au-dessus du seuil soft de robustesse.
4. Le signal Q4→CEA (Cohen-d + nuls + GEO) reste la preuve utile ; le full v6 en mode progression/cascade reste **exploratoire / fragile** sur cet axe.

## Fichiers
- `pipeline_runs/v6_kras_high/master_results.json`
- `universal_master_report.txt`
- checkpoints 01–03

*Conclusion : le contraste binaire confirme le même profil L7 FRAGILE ; prioriser pureté ESTIMATE / documentation du signal Q4 plutôt qu’un 3e run continuum.*
