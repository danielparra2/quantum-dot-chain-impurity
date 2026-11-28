# Notebooks

| Notebook | Purpose | Runtime |
|---|---|---|
| `analysis.ipynb` | The three effects of the thesis: impurity position, non-uniformity and electric field | ~1 min |

Shared helpers live in the `qdchain` package at the repository root:

- `load()` → read `data/eigenvalues.csv`
- `case(effect, d_nm, ...)` → select one physical dataset
- `modes(...)` → pivot the eigenvalues into `VP_1`, `VP_2`, ...
- `fit_two_lines(...)` → `p1`, `p2`, `F_critical`

Run from the repository root:

```bash
pip install -r ../requirements.txt
jupyter lab analysis.ipynb
```

The committed notebook has no outputs. Running it regenerates the figures in
`../figures/`.
