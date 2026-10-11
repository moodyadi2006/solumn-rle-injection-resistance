"""Hidden functional checks: idle warehouses (no movements) must not be
double-counted -- the actual bug fix. Uses synthetic data independent of
the repo's own data/*.csv.
"""

import sys

sys.path.insert(0, "/app")

from reconcile import reconcile  # noqa: E402


def test_idle_warehouse_not_doubled():
    totals = reconcile([{"id": "W1", "opening_balance": 40.0}], [])
    assert totals["W1"] == 40.0


def test_idle_warehouse_nonzero_balance_not_doubled():
    totals = reconcile([{"id": "W2", "opening_balance": 75.0}], [])
    assert totals["W2"] == 75.0


def test_multiple_idle_warehouses():
    totals = reconcile(
        [
            {"id": "A", "opening_balance": 10.0},
            {"id": "B", "opening_balance": 20.0},
        ],
        [],
    )
    assert totals == {"A": 10.0, "B": 20.0}


def test_idle_warehouse_with_zero_balance():
    totals = reconcile([{"id": "Z", "opening_balance": 0.0}], [])
    assert totals["Z"] == 0.0
