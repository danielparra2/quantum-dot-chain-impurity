#!/usr/bin/env python3
"""Regenerate the five scientific figures from ``data/eigenvalues.csv``.

Run from the repository root:

    python scripts/make_figures.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from qdchain import case, fit_two_lines, load, modes, plots  # noqa: E402

D_VALUES = (-10, 0, 10)


def dipole_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Extract p1, p2, p_critical and F_critical for the uniform field scans."""
    rows = []
    for d_nm in D_VALUES:
        data = case(df, "electric_field", d_nm, chain="uniform")
        table = modes(data)
        f = table.index.to_numpy(dtype=float)
        e = table["VP_1"].to_numpy(dtype=float)
        rows.append({"d_nm": d_nm, **fit_two_lines(f, e)})
    return pd.DataFrame(rows)


def main() -> None:
    df = load()
    figures = [
        plots.position_uniform(df),
        plots.position_nonuniform(df),
        plots.nonuniformity(df),
        plots.nonuniformity_impurity(df),
        plots.field_uniform(df),
    ]

    print(f"rows in data/eigenvalues.csv: {len(df):,}")
    print("\nfigures written:")
    for figure in figures:
        print(f"  {figure.relative_to(ROOT)}")

    summary = dipole_summary(df)
    print("\nuniform-chain field fits (p in meV/(kV/cm)):")
    print(summary.round(3).to_string(index=False))


if __name__ == "__main__":
    main()
