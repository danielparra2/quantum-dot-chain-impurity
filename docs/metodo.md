# Method and numerical model

This note documents the physical model, the COMSOL configuration and the export format behind
the data in `data/`. It is meant to make the repository reproducible without the original thesis
manuscript.

## 1. Physical model

A single donor impurity (charge `+e`) sits inside a linear chain of five laterally coupled
quantum dots. The electron is described in the **effective-mass approximation** by a 2D
Schrödinger equation:

```
H ψ = E ψ
H = -ħ²/(2m*) ∇² + V_conf(r) - e²/(4π ε0 εr |r - r_i|) + e F·r
```

- `m*` is the effective mass of the conduction electron.
- `εr` is the static relative permittivity of the host material.
- `V_conf(r)` is the band-offset confinement produced by the GaAs/AlGaAs heterostructure.
- `r_i` is the in-plane impurity position along the chain axis.
- `F` is an external electric field applied along the chain.

The isolated-donor limit is the 2D hydrogenic problem,

```
E_n = -Ry* / (n + 1/2)²,      Ry* = ħ² / (2 m* a*²),      a* = 4π ε0 εr ħ² / (m* e²).
```

For GaAs (`m* = 0.067 m0`, `εr = 12.9`): `a* ≈ 10.19 nm`, `Ry* ≈ 5.478 meV`, and the ground
state sits at `E_0 = -21.90 meV`.

## 2. Material parameters used in COMSOL

The parameter file is preserved verbatim in [`parametros_comsol.txt`](parametros_comsol.txt).
The relevant entries are:

| Parameter | Value / expression | Meaning |
|---|---|---|
| `Xo` | 0.3 | Al mole fraction in the AlGaAs matrix |
| `mef_Ga` | `0.067 m0` | effective mass inside the GaAs dots |
| `mef_Al` | `(0.067 + 0.083 Xo) m0` | effective mass in the matrix |
| `E_Ga` | `12.9 ε0` | permittivity of GaAs |
| `E_Al` | `(12.9 - 2.84 Xo) ε0` | permittivity of AlGaAs |
| `V_Al` | `0.6 (1047 Xo + 470 Xo²) / 1000` | confinement potential, ≈ 213.84 meV |
| `R1` | 10 | dot radius (nm) |
| `Re` | `ro + 2 R1` | outer domain radius |
| `F` | 20 kV/cm | electric-field parameter (swept per dataset) |

The simulated domain is a disk of radius `Re ≈ 200 nm` with **Dirichlet** boundary condition
`ψ = 0` on the outer circle. This is large enough for the donor wavefunction to decay before
reaching the boundary (finite-size check: `R = 300 nm` changes the levels by less than
`10⁻³ meV`).

## 3. Mesh and discretization

- Unstructured triangular mesh with **geometric refinement towards the impurity**.
- The local element size follows `h(r) = min(h_max, α r)`, so the mesh is dense where the
  Coulomb potential varies fastest.
- Quadratic Lagrange elements (P2) for the wavefunction.
- The generalized eigenvalue problem `K u = E M u` is solved with a shift-invert eigensolver.
- The same strategy was reproduced from scratch in Python in the companion repository
  [`2d-hydrogen-atom-hydrogenic-impurity`](https://github.com/danielparra2/2d-hydrogen-atom-hydrogenic-impurity) to validate the method independently of COMSOL.

## 4. COMSOL export format

Each `.txt` file is a 1D export with exactly **8 header lines** followed by two columns:

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
...
```

The repository does not ship the raw exports. They were consolidated into a single
tidy table, `data/eigenvalues.csv`, with one row per eigenvalue:

| `sweep` | `sweep_value` | `sweep_unit` |
|---|---|---|
| `xi` | impurity position `x_i` | **nm** |
| `R5` | fifth-dot radius `R_5` | **nm** |
| `F` | electric field `F` | **kV/cm** |

The energy is stored in `E_eV` in **eV**. No rescaling or smoothing is applied
to the exports; the only conversion is metres to nanometres for readability.
The provenance of each source file is kept in `data/manifest.csv`.

## 5. Eigenvalue ordering

COMSOL returns eigenvalues unsorted for each value of the sweep variable. The table already
contains a `mode` column: at every sweep value the eigenvalues are sorted and numbered, so that
mode 1 is always the ground state, mode 2 the first excited state, and so on. `qdchain.modes`
pivots this column into `VP_1`, `VP_2`, ... This step is essential before plotting or comparing
curves.

## 6. Dipole analysis

The induced dipole moment is obtained from the slope of the ground-state energy with respect to
the field, `p = -dE/dF`. The analysis fits two straight lines on each side of the anticrossing:

```
m = Σ (x - x0)(y - y0) / Σ (x - x0)²
```

with the two segments joined at the local maximum `(x0, y0)` of the selected energy branch. The
fitted slopes are then converted to the `p1` / `p2` plateau values reported in the figures.

The implementation is shared in `qdchain/physics.py` (`fit_two_lines`) and demonstrated in
`notebooks/analysis.ipynb`.

## 7. Counterintuitive results

These are the results worth highlighting when explaining the thesis.

### 7.1 The symmetry rule (s vs p)

- **s-type** states have no node. Their energy is **minimum** when the impurity sits at the
  centre of a dot and **maximum** at the bottlenecks between dots.
- **p-type** states have one node. Their energy is **maximum** at the centre of a dot and
  **minimum** at the bottlenecks: the nodal plane fits naturally into the constriction, so each
  lobe occupies a neighbouring cavity.

This rule explains why the first excited state oscillates out of phase with the ground state in
`figures/EvsXiUniforme.png`.

### 7.2 The ground state is pinned by the donor

For every separation `d`, the ground state stays near **-21.41 meV**, very close to the isolated
2D donor (-21.90 meV). The donor dominates over the structural confinement almost everywhere;
the structure only matters at the chain ends and at the material changes (`d = 0, 10 nm`).

### 7.3 The critical field is inversely proportional to `d`

| `d` (nm) | `F_critical` (kV/cm) |
|---|---|
| -10 | 1.200 |
| 0 | 1.000 |
| 10 | 0.800 |

A more separated chain is **easier** to polarize. This is the opposite of the naive expectation
(more separation → stronger field). The reason is that the electron is already more confined in
the separated regime, so less field is needed to push it out.

### 7.4 The fifth dot can be a donor or an acceptor

- `R_5 < 30 nm`: the fifth dot is too small; it **gives** the electron to the other four. It acts
  as a **donor**.
- `R_5 = 30 nm`: the fifth level joins the first sub-band.
- `R_5 > 30 nm`: the fifth dot is the largest cavity; the electron **prefers** it. It acts as an
  **acceptor** and the level descends monotonically.

The asymmetry also affects the dipole hierarchy: in the symmetric chain `|p_1| < |p_2|`, but for
`R_5 = 50 nm` the relation can become `|p_1| > |p_2|`.

### 7.5 No real crossings: Von Neumann–Wigner

When the descending fifth level meets a chain state with the **same s-type symmetry**, the two
levels repel instead of crossing. This is the anticrossing around `R_5 = 35 nm` in
`figures/EvsR5_noImpureza_orbitales.png`. The orbitals hybridize and the charge transfer becomes
asymmetric.

## 8. Caveats

- The model is **2D** (in-plane confinement); it does not include the z-direction or strain.
- A single donor is considered; donor–donor interaction is absent.
- The external field is static and uniform.
- The Dirichlet boundary is an approximation; its error was checked against `R = 300 nm`.
- The figures are labelled in Spanish because they are the original thesis figures.
