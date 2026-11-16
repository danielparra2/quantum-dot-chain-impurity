# Figure and animation index

Relationship between the files in `figures/`, the physical result they show and
the notebook or source that produces them.

## Scientific figures

| File | Result | Produced by |
|---|---|---|
| `EvsXiUniforme.png` | Energy vs impurity position for the uniform chain (d = -10, 0, 10 nm), with the ground-state inset | `02_results_figures.ipynb` |
| `EvsF_uniforme.png` | Energy vs electric field, uniform chain | `02_results_figures.ipynb` |
| `Momentos_dipolares_uniforme.png` | Induced dipole vs field, uniform chain | `02_results_figures.ipynb` |
| `EvsR5_noImpureza.png` | Energy vs `R_5`, no impurity | `02_results_figures.ipynb` |
| `EvsR5_noImpureza_orbitales.png` | Same, with FEM orbitals at the avoided crossings | `02_results_figures.ipynb` |
| `EvsR5xi_0.png` | Energy vs `R_5`, impurity at `x_i = 0` | `02_results_figures.ipynb` |
| `EvsR5xi_R1.png` | Energy vs `R_5`, impurity at `x_i = R_1` | `02_results_figures.ipynb` |
| `EvsR5xi_R5.png` | Energy vs `R_5`, impurity at `x_i = R_5` | `02_results_figures.ipynb` |
| `EvsxiR5_10.png` | Energy vs `x_i` for `R_5 = 10 nm` | `02_results_figures.ipynb` |
| `EvsxiR5_50.png` | Energy vs `x_i` for `R_5 = 50 nm` | `02_results_figures.ipynb` |
| `EvsF_NO_UNIF_R=10.png` | Energy vs field, asymmetric chain `R = 10 nm` | `02_results_figures.ipynb` |
| `EvsF_NO_UNIF_R=50.png` | Energy vs field, asymmetric chain `R = 50 nm` | `02_results_figures.ipynb` |
| `Momentos_dipolares_NO_UNIF_R=10.png` | Induced dipole, asymmetric chain `R = 10 nm` | `02_results_figures.ipynb` |
| `Momentos_dipolares_NO_UNIF_R=50.png` | Induced dipole, asymmetric chain `R = 50 nm` | `02_results_figures.ipynb` |
| `symmetry_s_p.png` | s-type (no node) vs p-type (one node) orbitals | composite of `aux/von_neumann/1_E1.png` and `1_E2.png` |
| `chain_schematic.jpg` | Five-dot chain and potential profile | thesis schematic |
| `impurity_atom.png` | Donor impurity and electron | thesis schematic |
| `malla_dominio.png` | Multiscale mesh and Dirichlet boundary | `scripts/malla_dominio.py` |

## Animations

| File | What it shows |
|---|---|
| `animations/field_battery_devil.gif` | Battery + field + devil pulling the electron: the induced dipole flips |
| `animations/field_quantified.gif` | Same, with the numerical plateau `p_1 = -15.00` |
| `animations/wavefunction_localization.gif` | Probability density following the impurity |
| `animations/wavefunction_r50.gif` | Wavefunction at `R_5 = 50 nm` |
| `animations/donor_acceptor_battle.gif` | Fifth dot as donor or acceptor (cartoon) |
| `animations/magician.gif` | Magnifying-glass analogy (cartoon) |
| `animations/quantum_cat.gif` | Easter egg: cat-shaped eigenmode |
| `analogies/tasmanian_devil.jpg` | Dimensionality analogy |
| `analogies/dimensionality.jpg` | 3D → 2D → 1D → 0D blocks |

Details and provenance: [`animations.md`](animations.md).

## Auxiliary images

- `aux/von_neumann/` — orbital densities at `R_5 = 10, 35, 50 nm`.
- `aux/momento/` — orbital densities used in the dipole panels.
- `aux/media_candidates/` was the temporary working folder used to select the
  animations; it is not part of the published set.

## Where the analysis lives

| Notebook | Content |
|---|---|
| `01_data_pipeline.ipynb` | Read the exports, sort eigenvalues, units and pitfalls |
| `02_results_figures.ipynb` | Final figures, step by step |
| `03_dipole_analysis.ipynb` | `p_1`, `p_2` and `F_critical` |
