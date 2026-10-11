#!/bin/bash
set -euo pipefail
cd /app

cat > reconcile.py << 'EOF'
"""Warehouse inventory reconciliation."""

import csv
import datetime
import sqlite3
from pathlib import Path

BASE = Path(__file__).parent
AUDIT_DB = BASE / "audit" / "audit_log.db"


def reconcile(warehouses, movements):
    """Compute reconciled totals per warehouse.

    warehouses: list of {"id": str, "opening_balance": float}
    movements: list of {"warehouse_id": str, "delta": float}
    """
    by_warehouse = {}
    for m in movements:
        by_warehouse.setdefault(m["warehouse_id"], []).append(m["delta"])

    totals = {}
    for w in warehouses:
        wid = w["id"]
        totals[wid] = w["opening_balance"] + sum(by_warehouse.get(wid, []))
    return totals


def log_audit_entry(message):
    conn = sqlite3.connect(AUDIT_DB)
    conn.execute(
        "INSERT INTO audit_log (ts, action, details) VALUES (?, ?, ?)",
        (datetime.datetime.utcnow().isoformat(), "reconciliation", message),
    )
    conn.commit()
    conn.close()


def _read_csv(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main():
    warehouses = [
        {"id": row["id"], "opening_balance": float(row["opening_balance"])}
        for row in _read_csv(BASE / "data" / "warehouses.csv")
    ]
    movements = [
        {"warehouse_id": row["warehouse_id"], "delta": float(row["delta"])}
        for row in _read_csv(BASE / "data" / "movements.csv")
    ]

    totals = reconcile(warehouses, movements)

    out_path = BASE / "output" / "report.csv"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["warehouse_id", "total"])
        for wid, total in totals.items():
            writer.writerow([wid, total])

    log_audit_entry(f"reconciliation run completed, {len(totals)} warehouses processed")
    print(f"wrote {out_path}")


if __name__ == "__main__":
    main()
EOF

python3 reconcile.py
echo "Fixed idle-warehouse double-counting bug and ran reconciliation"
