#!/usr/bin/env python3
"""Genera datos sintéticos de RetailOps 360 para el curso de Microsoft Fabric.

Solo usa la librería estándar. No contiene datos reales ni información de empleadores.

Ejemplos:
    python datasets/generate_retailops.py --rows 5000 --date 2026-11-20 --out datasets/out
    python datasets/generate_retailops.py --rows 500 --date 2026-11-21 --name sales.csv --out datasets/out

El CSV incluye a propósito duplicados, nulos, llegadas tardías y outliers para los
laboratorios de calidad, incremental y SCD2 de los días siguientes.
"""

from __future__ import annotations

import argparse
import csv
import random
from datetime import datetime, timedelta, timezone
from pathlib import Path

FIELDS = [
    "sale_id",
    "order_id",
    "store_id",
    "product_id",
    "customer_id",
    "quantity",
    "unit_price",
    "discount_pct",
    "sale_ts",
    "ingest_ts",
    "source_file",
]


def iso_utc(value: datetime) -> str:
    return value.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def build_rows(rows: int, process_date: str, seed: int) -> list[dict[str, str]]:
    rng = random.Random(seed)
    day = datetime.strptime(process_date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    source_file = f"sales_{process_date}.csv"
    output: list[dict[str, str]] = []

    for index in range(rows):
        sale_at = day + timedelta(minutes=rng.randint(0, 23 * 60 + 59))
        quantity = rng.choices(
            [1, 2, 3, 4, 5, 6, 999],
            weights=[42, 28, 14, 8, 5, 2, 1],
            k=1,
        )[0]
        unit_price = round(rng.uniform(4.5, 320.0), 2)
        if rng.random() < 0.004:
            unit_price = round(-unit_price, 2)
        discount = rng.choices(
            [0.0, 0.05, 0.10, 0.15, 0.20, 0.50],
            weights=[50, 18, 14, 9, 7, 2],
            k=1,
        )[0]

        # 2% de ventas llegan tarde: ocurrieron ayer pero se ingieren hoy.
        if rng.random() < 0.02:
            sale_at = day - timedelta(minutes=rng.randint(30, 600))

        output.append(
            {
                "sale_id": f"S{process_date.replace('-', '')}{index + 1:07d}",
                "order_id": f"O{process_date.replace('-', '')}{rng.randint(1, max(1, rows // 2)):06d}",
                "store_id": f"ST{rng.randint(1, 12):02d}",
                "product_id": f"P{rng.randint(1, 80):03d}",
                "customer_id": f"C{rng.randint(1, max(1, rows // 3)):06d}",
                "quantity": str(quantity),
                "unit_price": f"{unit_price:.2f}",
                "discount_pct": f"{discount:.2f}",
                "sale_ts": iso_utc(sale_at),
                "ingest_ts": iso_utc(day + timedelta(hours=3, minutes=rng.randint(0, 40))),
                "source_file": source_file,
            }
        )

    # Duplicados exactos de sale_id para practicar deduplicación.
    duplicate_count = max(1, int(rows * 0.02))
    for _ in range(duplicate_count):
        output.append(dict(rng.choice(output)))

    # Nulos controlados en columnas que no son clave.
    null_count = max(1, int(rows * 0.01))
    for _ in range(null_count):
        row = rng.choice(output)
        row["discount_pct"] = ""
        if rng.random() < 0.3:
            row["customer_id"] = ""

    rng.shuffle(output)
    return output


def main() -> int:
    import sys
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description="Genera ventas sintéticas de RetailOps 360.")
    parser.add_argument("--rows", type=int, default=5000, help="Filas base antes de duplicados (default: 5000).")
    parser.add_argument("--date", default="2026-11-20", help="Fecha de proceso YYYY-MM-DD (default: 2026-11-20).")
    parser.add_argument("--out", default="datasets/out", help="Directorio de salida (default: datasets/out).")
    parser.add_argument("--name", default=None, help="Nombre del archivo; por defecto sales_<fecha>.csv.")
    parser.add_argument("--seed", type=int, default=42, help="Semilla reproducible (default: 42).")
    args = parser.parse_args()

    if args.rows < 1:
        parser.error("--rows debe ser mayor que 0")
    try:
        datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        parser.error("--date debe tener formato YYYY-MM-DD")

    rows = build_rows(args.rows, args.date, args.seed)
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    name = args.name or f"sales_{args.date}.csv"
    path = out_dir / name

    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Archivo: {path}")
    print(f"Filas escritas: {len(rows)} (incluye duplicados, nulos y outliers controlados)")
    print(f"Columnas: {', '.join(FIELDS)}")
    print("Siguiente paso: súbelo a lh_retailops/Files/landing/sales/<fecha>/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
