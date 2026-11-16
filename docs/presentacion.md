# Defense notes — the story in five slides

The defense deck (`EXPO_FINAL.pptx`) is not included in this repository. This
note preserves the narrative and the results that are easy to miss in a static
figure.

## 1. The hook

A quantum dot is an **artificial atom**: its properties are tunable through
geometry, material and external fields. A chain of five coupled dots adds a new
knob: the **coupling** between cavities.

## 2. The symmetry rule

The spectrum is organized by the symmetry of the states:

- **s-type** states have no node and minimize their energy at the centre of a
  dot.
- **p-type** states have one node and maximize their energy at the centre of a
  dot; they minimize at the bottlenecks, where the nodal plane fits the
  constriction.

This single rule explains why the first excited state oscillates out of phase
with the ground state in `figures/EvsXiUniforme.png`.

## 3. The counterintuitive field result

The critical field needed to delocalize the electron is **inversely
proportional to the inter-dot separation**:

| `d` (nm) | `F_critical` (kV/cm) |
|---|---|
| −10 | 1.200 |
| 0 | 1.000 |
| 10 | 0.800 |

A more separated chain is easier to polarize, because the electron is already
more confined. The naive expectation (more separation → more field) is wrong.

The induced dipole follows the same trend:

| `d` (nm) | `p₁` (meV/(kV/cm)) | `p₂` |
|---|---|---|
| −10 | −9.89 | 10.42 |
| 0 | −12.00 | 12.53 |
| 10 | −15.00 | 15.30 |

## 4. Structural asymmetry as a tuning knob

The fifth dot is the asymmetry. Its size decides whether it behaves as a
**donor** (`R₅ < 30 nm`) or an **acceptor** (`R₅ > 30 nm`). It also changes the
dipole hierarchy: for `R₅ = 50 nm` the relation can become `|p₁| > |p₂|`.

## 5. The anticrossing

When the fifth level descends and meets a chain state with the **same s-type
symmetry**, the two levels do not cross. They repel: the **Von Neumann–Wigner
anticrossing**. The orbitals hybridize and the charge transfer becomes
asymmetric. This is the mechanism behind the sharp dipole jump.

## What is in this repository

- The raw COMSOL eigenvalue exports.
- The Python analysis and the final figures.
- The animations used in the defense.
- The method, parameters and validation.

The written manuscript is kept in a separate repository.
