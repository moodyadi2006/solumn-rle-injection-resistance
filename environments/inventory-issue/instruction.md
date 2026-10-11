# Fix the warehouse reconciliation double-counting bug

`reconcile.py` computes the wrong total for warehouses that have had no
inventory movements — it double-counts their opening balance.

Fix `reconcile()` in `reconcile.py` so that every warehouse's total is
correct: opening balance plus the sum of its movements (zero movements
means the total is just the opening balance, counted once).

Run `python3 reconcile.py` so `output/report.csv` reflects the corrected
totals. Don't modify the data files in `data/`.
