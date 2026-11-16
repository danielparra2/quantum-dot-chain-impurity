# Data

Raw eigenvalue exports from COMSOL Multiphysics for the five-dot chain simulations.

- 32 `.txt` files, 8.3 MB total.
- Each file keeps its original COMSOL header (model, version, date, nodes).
- `manifest.csv` maps every file to its source model and physical case.
- `consolidado.csv.gz` is **not** committed; generate it with `scripts/consolidar.py` if you
  want a single tabular file.

## Format

```
% Model:              qd5=10_d=0.mph
% Version:            COMSOL 6.4.0.429
% Date:               Aug 23 2026, 12:19
% Dimension:          1
% Nodes:              4020
% Expressions:        1
% Description:        ...
% Length unit:        m
<X> <eigenvalue>
```

The first column is the sweep variable and the second is the eigenvalue in eV.

| Sweep variable | Unit | Typical range |
|---|---|---|
| impurity position `x_i` | m | `-1.8e-7 … 2.1e-7` |
| inter-dot distance `R_5` | m | `1e-8 … 6e-8` |
| electric field `F` | kV/cm | `-5 … 10` |

Do **not** merge the files by hand: the per-file headers are the provenance record. Use
`manifest.csv` (already tracked) or run:

```bash
python scripts/consolidar.py
```

which writes a gzip-compressed CSV with an extra `file` column.

## Regenerating the manifest

```bash
python scripts/generar_manifest.py
```

The script only reads the first 8 lines of each file plus the data columns; it does not modify
the exports.
