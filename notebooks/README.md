# Notebooks

Run them in this order:

| # | Notebook | Purpose | Runtime |
|---|---|---|---|
| 01 | `01_data_pipeline.ipynb` | Read the 32 COMSOL exports, inspect the headers, sort eigenvalues into modes. | seconds |
| 02 | `02_results_figures.ipynb` | Rebuild the final thesis figures. | ~1 min |
| 03 | `03_dipole_analysis.ipynb` | Extract `p₁`, `p₂` and `F_critical` with the two-line fit. | seconds |

Shared helpers live in `chain_utils.py`:

- `read_comsol(path)` → `(DataFrame, header)`
- `load_all()` → `(dict of DataFrames, provenance DataFrame)`
- `organize(df)` → mode-sorted table (`VP_1`, `VP_2`, ...)
- `fit_two_lines(df)` → `p₁`, `p₂`, `F_critical`

## Data conventions

- Every `.txt` has **8 header lines** followed by two columns: `X` and `eigenvalue` (eV).
- `X` is in **metres** for position scans and in **kV/cm** for field scans.
- The raw files are never modified by the notebooks.

## Run

```bash
pip install -r ../requirements.txt
jupyter lab 01_data_pipeline.ipynb
```

## Note

The committed notebooks have **no outputs**. Running them regenerates the
figures and writes them to `../figures/`. The published PNGs are already in
the repository, so you do not need to run anything to read the results.
