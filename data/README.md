# Data

One tidy table with the eigenvalue exports from COMSOL Multiphysics for the
five-dot chain simulations.

## `eigenvalues.csv`

One row per eigenvalue. 117,335 rows from 18 COMSOL exports.

| Column | Meaning |
|---|---|
| `effect` | `impurity_position`, `non_uniformity` or `electric_field` |
| `chain` | `uniform` or `non_uniform` |
| `d_nm` | inter-dot gap, in nanometres |
| `R5_nm` | fifth-dot radius when it is fixed (empty otherwise) |
| `xi_nm` | impurity position when it is fixed (empty if swept or absent) |
| `sweep` | swept variable: `xi`, `R5` or `F` |
| `sweep_value` | value of the swept variable, in `sweep_unit` |
| `sweep_unit` | `nm` for positions and radii, `kV/cm` for the field |
| `mode` | eigenvalue rank at a fixed sweep value (1 = ground state) |
| `E_eV` | eigenvalue in electron-volts |
| `source_file` | original COMSOL export |

The positions and radii are stored in nanometres, not metres, so the table can
be read directly. The modes are sorted at every sweep value: `mode = 1` is
always the ground state.

## `manifest.csv`

Provenance of the 18 source exports: COMSOL model, version, export date, case,
quantity, row count and the swept range. The raw `.txt` files are not included
in the repository.

## Reproducing the analysis

```bash
python scripts/make_figures.py
jupyter lab notebooks/analysis.ipynb
```
