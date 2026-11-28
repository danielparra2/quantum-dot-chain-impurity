"""Figures used in the README and in the analysis notebook."""

from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .data import case, modes

FIGS = Path(__file__).resolve().parent.parent / "figures"
D_VALUES = (-10, 0, 10)
R5_VALUES = (10.0, 50.0)
N_MODES = 10
COLORS = plt.get_cmap("viridis")(np.linspace(0.10, 0.85, N_MODES))

plt.rcParams.update(
    {
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "axes.edgecolor": "#333333",
        "axes.linewidth": 0.9,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
    }
)


def _style(ax: plt.Axes) -> None:
    ax.grid(True, alpha=0.25, linewidth=0.6)
    ax.tick_params(direction="out", length=3)


def _plot_modes(ax: plt.Axes, table: pd.DataFrame, nmax: int = N_MODES) -> None:
    columns = list(table.columns)[:nmax]
    x = table.index.to_numpy()
    for index, column in enumerate(columns):
        ax.plot(x, table[column].to_numpy() * 1000.0, color=COLORS[index], lw=1.4)


def _save(fig: plt.Figure, out: str | Path) -> Path:
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=200, bbox_inches="tight")
    plt.close(fig)
    return out


def position_uniform(df: pd.DataFrame, out: str | Path = FIGS / "EvsXiUniforme.png") -> Path:
    """Energy versus impurity position for the uniform chain."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.0), sharey=False)
    for ax, d_nm in zip(axes, D_VALUES):
        data = case(df, "impurity_position", d_nm, chain="uniform")
        _plot_modes(ax, modes(data))
        ax.set_title(f"d = {d_nm} nm")
        ax.set_xlabel(r"$x_i$ (nm)")
        _style(ax)
    axes[0].set_ylabel("Energy (meV)")
    fig.suptitle("Energy vs impurity position (uniform chain)", fontsize=13, y=1.02)
    fig.tight_layout()
    return _save(fig, out)


def position_nonuniform(df: pd.DataFrame, out: str | Path = FIGS / "EvsxiR5.png") -> Path:
    """Energy versus impurity position for the non-uniform chain."""
    fig, axes = plt.subplots(3, 2, figsize=(10, 10), sharex="col")
    for row, d_nm in enumerate(D_VALUES):
        for column, R5 in enumerate(R5_VALUES):
            ax = axes[row, column]
            data = case(df, "impurity_position", d_nm, chain="non_uniform", R5_nm=R5)
            _plot_modes(ax, modes(data))
            ax.set_title(f"d = {d_nm} nm, R5 = {R5:.0f} nm")
            ax.set_xlabel(r"$x_i$ (nm)")
            _style(ax)
        axes[row, 0].set_ylabel("Energy (meV)")
    fig.suptitle("Energy vs impurity position (non-uniform chain)", fontsize=13, y=1.00)
    fig.tight_layout()
    return _save(fig, out)


def nonuniformity(df: pd.DataFrame, out: str | Path = FIGS / "EvsR5_noImpureza.png") -> Path:
    """Energy versus the fifth-dot radius, without impurity."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.0), sharey=False)
    for ax, d_nm in zip(axes, D_VALUES):
        data = case(df, "non_uniformity", d_nm, impurity=False)
        _plot_modes(ax, modes(data))
        ax.axvline(30.0, color="#888888", ls="--", lw=0.9)
        ax.set_title(f"d = {d_nm} nm")
        ax.set_xlabel(r"$R_5$ (nm)")
        _style(ax)
    axes[0].set_ylabel("Energy (meV)")
    fig.suptitle("Energy vs fifth-dot radius (no impurity)", fontsize=13, y=1.02)
    fig.tight_layout()
    return _save(fig, out)


def nonuniformity_impurity(df: pd.DataFrame, out: str | Path = FIGS / "EvsR5xi_0.png") -> Path:
    """Energy versus the fifth-dot radius, with the impurity at the centre."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.0), sharey=False)
    for ax, d_nm in zip(axes, D_VALUES):
        data = case(df, "non_uniformity", d_nm, impurity=True)
        _plot_modes(ax, modes(data))
        ax.axvline(30.0, color="#888888", ls="--", lw=0.9)
        ax.set_title(f"d = {d_nm} nm")
        ax.set_xlabel(r"$R_5$ (nm)")
        _style(ax)
    axes[0].set_ylabel("Energy (meV)")
    fig.suptitle(r"Energy vs fifth-dot radius (impurity at $x_i = 0$)", fontsize=13, y=1.02)
    fig.tight_layout()
    return _save(fig, out)


def field_uniform(df: pd.DataFrame, out: str | Path = FIGS / "EvsF_uniforme.png") -> Path:
    """Energy versus electric field for the uniform chain."""
    fig, axes = plt.subplots(1, 3, figsize=(12, 4.0), sharey=False)
    for ax, d_nm in zip(axes, D_VALUES):
        data = case(df, "electric_field", d_nm, chain="uniform")
        _plot_modes(ax, modes(data))
        ax.set_title(f"d = {d_nm} nm")
        ax.set_xlabel(r"$F$ (kV/cm)")
        _style(ax)
    axes[0].set_ylabel("Energy (meV)")
    fig.suptitle("Energy vs electric field (uniform chain)", fontsize=13, y=1.02)
    fig.tight_layout()
    return _save(fig, out)
