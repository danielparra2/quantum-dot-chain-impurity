"""Build an optional single-file dataset from the COMSOL exports.

Output: data/consolidado.csv.gz with columns
    file, x, eigenvalue

The original .txt files are kept untouched.
"""

from __future__ import annotations

import gzip
import csv
from pathlib import Path

AQUI = Path(__file__).resolve().parent.parent
DATA = AQUI / "data"
SALIDA = DATA / "consolidado.csv.gz"


def main() -> None:
    total = 0
    with gzip.open(SALIDA, "wt", newline="", encoding="utf-8") as out:
        writer = csv.writer(out)
        writer.writerow(["file", "x", "eigenvalue"])
        for path in sorted(DATA.glob("*.txt")):
            with path.open(encoding="utf-8", errors="replace") as fh:
                for _ in range(8):
                    fh.readline()
                for linea in fh:
                    partes = linea.split()
                    if len(partes) < 2:
                        continue
                    try:
                        x = float(partes[0])
                        e = float(partes[1])
                    except ValueError:
                        continue
                    writer.writerow([path.name, x, e])
                    total += 1
    print(f"{total} rows -> {SALIDA}")


if __name__ == "__main__":
    main()
