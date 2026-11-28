"""Analysis helpers for the five-dot chain thesis.

The public API is intentionally small:

    from qdchain import load, case, modes, fit_two_lines

``load`` reads the single tidy table ``data/eigenvalues.csv``; ``case`` selects
one physical dataset; ``modes`` pivots the eigenvalues into modes ``VP_1``,
``VP_2``, ...; ``fit_two_lines`` extracts the induced-dipole plateaus and the
critical field from an energy-versus-field scan.
"""

from .data import DATA, case, load, modes
from .physics import fit_two_lines, induced_dipole
from . import plots

__all__ = [
    "DATA",
    "load",
    "case",
    "modes",
    "fit_two_lines",
    "induced_dipole",
    "plots",
]
