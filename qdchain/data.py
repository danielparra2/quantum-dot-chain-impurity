"""Load and select the tidy eigenvalue table."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

DATA = Path(__file__).resolve().parent.parent / "data" / "eigenvalues.csv"

REQUIRED = [
    "effect",
    "chain",
    "d_nm",
    "R5_nm",
    "xi_nm",
    "sweep",
    "sweep_value",
    "sweep_unit",
    "mode",
    "E_eV",
    "source_file",
]


def load(path: str | Path = DATA) -> pd.DataFrame:
    """Read ``data/eigenvalues.csv`` and validate its columns."""
    df = pd.read_csv(path)
    missing = [column for column in REQUIRED if column not in df.columns]
    if missing:
        raise ValueError(f"missing columns in {path}: {missing}")
    return df


def case(
    df: pd.DataFrame,
    effect: str,
    d_nm: int,
    chain: str | None = None,
    R5_nm: float | None = None,
    impurity: bool | None = None,
) -> pd.DataFrame:
    """Select one physical dataset.

    Parameters
    ----------
    effect : {"impurity_position", "non_uniformity", "electric_field"}
    d_nm : int
        Inter-dot gap, in nanometres.
    chain : {"uniform", "non_uniform"}, optional
    R5_nm : float, optional
        Fifth-dot radius for the non-uniform position scans.
    impurity : bool, optional
        ``True`` keeps the cases with a donor, ``False`` the cases without one.
    """
    mask = (df["effect"] == effect) & (df["d_nm"] == d_nm)
    if chain is not None:
        mask &= df["chain"] == chain
    if R5_nm is not None:
        mask &= df["R5_nm"] == R5_nm
    if impurity is True:
        mask &= df["xi_nm"].notna()
    elif impurity is False:
        mask &= df["xi_nm"].isna()
    return df[mask].copy()


def modes(df: pd.DataFrame) -> pd.DataFrame:
    """Pivot one case into modes ``VP_1``, ``VP_2``, ... indexed by sweep value."""
    table = df.pivot_table(
        index="sweep_value",
        columns="mode",
        values="E_eV",
        aggfunc="first",
    ).sort_index()
    table.columns = [f"VP_{int(column)}" for column in table.columns]
    return table
