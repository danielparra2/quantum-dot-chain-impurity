"""Shared helpers for the tutorial notebooks.

The COMSOL exports contain eight header lines followed by two columns:
the sweep variable ``X`` and the eigenvalue in eV.  These helpers keep the
notebooks short and make the data conventions explicit.
"""

from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data"


def read_comsol(path: str | Path) -> tuple[pd.DataFrame, dict[str, str]]:
    """Read one COMSOL 1D export.

    Returns
    -------
    df : DataFrame with columns ``X`` and ``eigenvalue``.
    header : dict with model, version, date, nodes, etc.
    """
    path = Path(path)
    header: dict[str, str] = {}
    with path.open(encoding="utf-8", errors="replace") as fh:
        for _ in range(8):
            line = fh.readline()
            match = re.match(r"%\s*([^:]+):\s*(.*)", line.strip())
            if match:
                header[match.group(1).strip().lower()] = match.group(2).strip()

    df = pd.read_csv(
        path,
        skiprows=8,
        sep=r"\s+",
        names=["X", "eigenvalue"],
        engine="python",
    )
    return df, header


def load_all(folder: str | Path = DATA) -> tuple[dict[str, pd.DataFrame], pd.DataFrame]:
    """Load every ``.txt`` export and return a provenance table."""
    folder = Path(folder)
    files: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, object]] = []

    for path in sorted(folder.glob("*.txt")):
        df, header = read_comsol(path)
        files[path.name] = df
        rows.append(
            {
                "file": path.name,
                "model": header.get("model", ""),
                "version": header.get("version", ""),
                "date": header.get("date", ""),
                "rows": len(df),
                "x_min": float(df["X"].min()),
                "x_max": float(df["X"].max()),
            }
        )

    return files, pd.DataFrame(rows)


def organize(df: pd.DataFrame) -> pd.DataFrame:
    """Sort the eigenvalues of each sweep point and pivot them into modes.

    COMSOL returns an unordered list of eigenvalues for every value of the
    sweep variable.  Sorting by ``(X, eigenvalue)`` and counting with
    ``cumcount`` guarantees that column ``VP_1`` is always the ground state,
    ``VP_2`` the first excited state, and so on.
    """
    out = df.copy()
    out = out.sort_values(by=["X", "eigenvalue"]).reset_index(drop=True)
    out["mode"] = out.groupby("X").cumcount()
    out = out.pivot(index="X", columns="mode", values="eigenvalue")
    out.columns = [f"VP_{i + 1}" for i in out.columns]
    return out.reset_index()


def fit_two_lines(
    df: pd.DataFrame,
    f_min: float = -1.1,
    f_max: float = 2.0,
) -> dict[str, float]:
    """Fit two straight lines to the ground-state energy around the anticrossing.

    The two segments are joined at the local maximum of the selected branch.
    The slope ``p = -dE/dF`` is returned in meV/(kV/cm), the units used in
    the thesis figures.
    """
    f = np.asarray(df["X"], dtype=float)
    e = np.asarray(df.iloc[:, 1], dtype=float)

    mask = (f >= f_min) & (f <= f_max)
    fm, em = f[mask], e[mask]
    if len(fm) < 3:
        raise ValueError("Not enough points in the fitting window.")

    i0 = int(np.argmax(em))
    f0, e0 = fm[i0], em[i0]

    def forced_slope(x: np.ndarray, y: np.ndarray) -> float:
        return float(np.sum((x - f0) * (y - e0)) / np.sum((x - f0) ** 2))

    f1, e1 = fm[: i0 + 1], em[: i0 + 1]
    f2, e2 = fm[i0:], em[i0:]
    m1 = forced_slope(f1, e1)
    m2 = forced_slope(f2, e2)

    return {
        "p1": -m1 * 1000.0,
        "p2": -m2 * 1000.0,
        "F_critical": float(f0),
        "E_critical": float(e0),
    }
