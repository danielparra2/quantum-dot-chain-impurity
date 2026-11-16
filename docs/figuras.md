# Figure map

Relationship between the final PNGs in `figures/`, the physical result they show, and the
notebook that produces them.

| File | Thesis result | Notebook |
|---|---|---|
| `EvsXiUniforme.png` | Energy vs impurity position for the uniform chain (d = -10, 0, 10 nm), with ground-state inset | `02_figuras_tesis.ipynb` |
| `EvsF_uniforme.png` | Energy vs electric field, uniform chain | `02_figuras_tesis.ipynb` |
| `Momentos_dipolares_uniforme.png` | Induced dipole vs field, uniform chain | `02_figuras_tesis.ipynb` |
| `EvsR5_noImpureza.png` | Energy vs `R_5`, no impurity | `02_figuras_tesis.ipynb` |
| `EvsR5_noImpureza_orbitales.png` | Same, with FEM orbitals at avoided crossings | `02_figuras_tesis.ipynb` |
| `EvsR5xi_0.png` | Energy vs `R_5`, impurity at `x_i = 0` | `02_figuras_tesis.ipynb` |
| `EvsR5xi_R1.png` | Energy vs `R_5`, impurity at `x_i = R_1` | `02_figuras_tesis.ipynb` |
| `EvsR5xi_R5.png` | Energy vs `R_5`, impurity at `x_i = R_5` | `02_figuras_tesis.ipynb` |
| `EvsxiR5_10.png` | Energy vs `x_i` for `R_5 = 10 nm` | `02_figuras_tesis.ipynb` |
| `EvsxiR5_50.png` | Energy vs `x_i` for `R_5 = 50 nm` | `02_figuras_tesis.ipynb` |
| `EvsF_NO_UNIF_R=10.png` | Energy vs field, asymmetric chain `R = 10 nm` | `02_figuras_tesis.ipynb` |
| `EvsF_NO_UNIF_R=50.png` | Energy vs field, asymmetric chain `R = 50 nm` | `02_figuras_tesis.ipynb` |
| `Momentos_dipolares_NO_UNIF_R=10.png` | Induced dipole, asymmetric chain `R = 10 nm` | `02_figuras_tesis.ipynb` |
| `Momentos_dipolares_NO_UNIF_R=50.png` | Induced dipole, asymmetric chain `R = 50 nm` | `02_figuras_tesis.ipynb` |
| `malla_dominio.png` | Schematic of the multiscale mesh and Dirichlet boundary | `scripts/malla_dominio.py` |

Auxiliary images used as insets inside the figures:

- `figures/aux/von_neumann/` — orbital probability densities at `R_5 = 10, 35, 50 nm`.
- `figures/aux/momento/` — orbital densities used in the dipole panels.

The exploratory notebook `01_analisis_exploratorio.ipynb` contains the full path from raw data to
mode-sorted curves, the two-line fits and the intermediate dipole plots.
