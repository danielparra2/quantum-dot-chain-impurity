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
  `hydrogenic-atom-2d-fem` (in preparation) to validate the method independently of COMSOL.

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

The notebooks read the files with:

```python
pd.read_csv(path, skiprows=8, sep=r"\s+", names=["X", "Valor_propio"], engine="python")
```

### Units of the first column

| Dataset family | `X` meaning | Unit |
|---|---|---|
| `caso*.txt`, `EvsxiR5=*.txt` | impurity position `x_i` | **m** (notebook converts to nm) |
| `EvsR5*.txt` | inter-dot distance `R_5` | **m** (notebook converts to nm) |
| `c*_F.txt`, `AEvsF*.txt` | electric field `F` | **kV/cm** |

The second column is the eigenvalue in **eV**. No rescaling or smoothing is applied to the raw
exports.

## 5. Eigenvalue ordering

COMSOL returns eigenvalues unsorted for each value of the sweep variable. The notebooks sort by
`(X, eigenvalue)` and assign mode indices with a cumulative count, so that mode 1 is always the
ground state, mode 2 the first excited state, and so on. This step is essential before plotting
or comparing curves.

## 6. Dipole analysis

The induced dipole moment is obtained from the slope of the ground-state energy with respect to
the field, `p = -dE/dF`. The analysis fits two straight lines on each side of the anticrossing:

```
m = Σ (x - x0)(y - y0) / Σ (x - x0)²
```

with the two segments joined at the local maximum `(x0, y0)` of the selected energy branch. The
fitted slopes are then converted to the `p1` / `p2` plateau values reported in the figures.

## 7. Caveats

- The model is **2D** (in-plane confinement); it does not include the z-direction or strain.
- A single donor is considered; donor–donor interaction is absent.
- The external field is static and uniform.
- The Dirichlet boundary is an approximation; its error was checked against `R = 300 nm`.
- The figures are labelled in Spanish because they are the original thesis figures.
