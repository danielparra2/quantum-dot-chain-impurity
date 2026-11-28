"""Physics extracted from the energy scans."""

from __future__ import annotations

import numpy as np
import pandas as pd


def induced_dipole(f: np.ndarray, e: np.ndarray) -> np.ndarray:
    """Return ``p = -dE/dF`` in meV/(kV/cm)."""
    f = np.asarray(f, dtype=float)
    e = np.asarray(e, dtype=float)
    return -np.gradient(e, f) * 1000.0


def fit_two_lines(
    f: np.ndarray,
    e: np.ndarray,
    f_min: float = -1.1,
    f_max: float = 2.0,
) -> dict[str, float]:
    """Fit two straight lines to the ground state around the anticrossing.

    The two segments meet at the local maximum of the selected branch. The
    slopes are returned as ``p1`` and ``p2`` in meV/(kV/cm), together with the
    field and energy of the critical point.
    """
    f = np.asarray(f, dtype=float)
    e = np.asarray(e, dtype=float)
    mask = (f >= f_min) & (f <= f_max)
    fm, em = f[mask], e[mask]
    if len(fm) < 3:
        raise ValueError("not enough points in the fitting window")

    i0 = int(np.argmax(em))
    f0, e0 = fm[i0], em[i0]

    def forced_slope(x: np.ndarray, y: np.ndarray) -> float:
        denominator = np.sum((x - f0) ** 2)
        if denominator == 0:
            raise ValueError("degenerate fitting window")
        return float(np.sum((x - f0) * (y - e0)) / denominator)

    m1 = forced_slope(fm[: i0 + 1], em[: i0 + 1])
    m2 = forced_slope(fm[i0:], em[i0:])

    return {
        "p1": -m1 * 1000.0,
        "p2": -m2 * 1000.0,
        "F_critical": float(f0),
        "E_critical": float(e0),
    }
