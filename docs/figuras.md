# Figure and animation index

Relationship between the files in `figures/`, the physical result they show and
the code that produces them.

## Scientific figures

| File | Result | Produced by |
|---|---|---|
| `EvsXiUniforme.png` | Energy vs impurity position for the uniform chain (d = -10, 0, 10 nm) | `scripts/make_figures.py` |
| `EvsxiR5.png` | Energy vs impurity position for the non-uniform chain (`R5 = 10` and `50 nm`) | `scripts/make_figures.py` |
| `EvsR5_noImpureza.png` | Energy vs `R5`, no impurity | `scripts/make_figures.py` |
| `EvsR5xi_0.png` | Energy vs `R5`, impurity at `x_i = 0` | `scripts/make_figures.py` |
| `EvsF_uniforme.png` | Energy vs electric field, uniform chain | `scripts/make_figures.py` |

## Static schematics and composites

| File | Content |
|---|---|
| `EvsR5_noImpureza_orbitales.png` | Same scan as above, with COMSOL orbital insets at the avoided crossings (thesis composite) |
| `symmetry_s_p.png` | s-type (no node) vs p-type (one node) orbitals |
| `chain_schematic.jpg` | Five-dot chain and potential profile (thesis schematic) |
| `impurity_atom.png` | Donor impurity and electron (thesis schematic) |
| `malla_dominio.png` | Multiscale mesh and Dirichlet boundary, from `scripts/malla_dominio.py` |

## Animations

| File | What it shows |
|---|---|
| `animations/field_battery_devil.gif` | Battery + field + devil pulling the electron: the induced dipole flips |
| `animations/field_quantified.gif` | Same, with the numerical plateau `p_1 = -15.00` |
| `animations/wavefunction_localization.gif` | Probability density following the impurity |
| `animations/wavefunction_r50.gif` | Wavefunction at `R5 = 50 nm` |
| `animations/nonuniform_chain.gif` | Wavefunction evolution as `R5` changes |
| `animations/donor_acceptor_battle.gif` | Fifth dot as donor or acceptor (cartoon) |
| `animations/magician.gif` | Magnifying-glass analogy (cartoon) |
| `animations/quantum_cat.gif` | Easter egg: cat-shaped eigenmode |
| `analogies/tasmanian_devil.jpg` | Dimensionality analogy |
| `analogies/dimensionality.jpg` | 3D → 2D → 1D → 0D blocks |

## Where the analysis lives

| File | Content |
|---|---|
| `qdchain/` | `data.py` (load and select), `physics.py` (`fit_two_lines`, dipole), `plots.py` (figures) |
| `scripts/make_figures.py` | Regenerates the five scientific figures and prints the dipole summary |
| `notebooks/analysis.ipynb` | The three effects of the thesis, step by step |
