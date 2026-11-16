"""Rebuild data/manifest.csv from the COMSOL headers.

Reads only the header lines and the two data columns of each .txt file.
The exports are never modified.
"""

from __future__ import annotations

import csv
import re
from pathlib import Path

AQUI = Path(__file__).resolve().parent.parent
DATA = AQUI / "data"

CASES = {
    "caso1.txt": ("Uniform chain", "Energy vs impurity position"),
    "caso2.txt": ("Uniform chain", "Energy vs impurity position"),
    "caso2_2.txt": ("Uniform chain", "Energy vs impurity position"),
    "caso3.txt": ("Uniform chain", "Energy vs impurity position"),
    "c1_F.txt": ("Uniform chain", "Energy vs electric field"),
    "c2_F.txt": ("Uniform chain", "Energy vs electric field"),
    "c2_2_F.txt": ("Uniform chain", "Energy vs electric field"),
    "c3_F.txt": ("Uniform chain", "Energy vs electric field"),
}


def describir(nombre: str) -> tuple[str, str]:
    if nombre in CASES:
        return CASES[nombre]
    if nombre.startswith("EvsR5sind"):
        return "Non-uniform chain (no impurity)", "Energy vs R5"
    if nombre.startswith("EvsR5xi=0"):
        return "Non-uniform chain (impurity at xi=0)", "Energy vs R5"
    if nombre.startswith("EvsR5xi=R1"):
        return "Non-uniform chain (impurity at xi=R1)", "Energy vs R5"
    if nombre.startswith("EvsR5xi=R5"):
        return "Non-uniform chain (impurity at xi=R5)", "Energy vs R5"
    if nombre.startswith("EvsxiR5=10"):
        return "Non-uniform chain, R5=10 nm", "Energy vs impurity position"
    if nombre.startswith("EvsxiR5=50"):
        return "Non-uniform chain, R5=50 nm", "Energy vs impurity position"
    if nombre.startswith("AEvsF"):
        return "Asymmetric chain", "Energy vs electric field"
    return "Unknown", "Unknown"


def leer_cabecera(path: Path) -> dict[str, str]:
    campos = {}
    with path.open(encoding="utf-8", errors="replace") as fh:
        for _ in range(8):
            linea = fh.readline()
            m = re.match(r"%\s*([^:]+):\s*(.*)", linea.strip())
            if m:
                campos[m.group(1).strip().lower()] = m.group(2).strip()
    return campos


def leer_rango(path: Path) -> tuple[int, float | None, float | None]:
    n = 0
    xmin = xmax = None
    with path.open(encoding="utf-8", errors="replace") as fh:
        for _ in range(8):
            fh.readline()
        for linea in fh:
            partes = linea.split()
            if len(partes) < 2:
                continue
            try:
                x = float(partes[0])
                float(partes[1])
            except ValueError:
                continue
            n += 1
            xmin = x if xmin is None else min(xmin, x)
            xmax = x if xmax is None else max(xmax, x)
    return n, xmin, xmax


def main() -> None:
    filas = []
    for path in sorted(DATA.glob("*.txt")):
        cab = leer_cabecera(path)
        n, xmin, xmax = leer_rango(path)
        caso, magnitud = describir(path.name)
        filas.append(
            [
                path.name,
                cab.get("model", ""),
                cab.get("version", ""),
                cab.get("date", ""),
                caso,
                magnitud,
                n,
                f"{xmin:.6g}" if xmin is not None else "",
                f"{xmax:.6g}" if xmax is not None else "",
            ]
        )

    destino = DATA / "manifest.csv"
    with destino.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "file",
                "comsol_model",
                "comsol_version",
                "export_date",
                "case",
                "quantity",
                "rows",
                "x_min",
                "x_max",
            ]
        )
        writer.writerows(filas)
    print(f"{len(filas)} files -> {destino}")


if __name__ == "__main__":
    main()
