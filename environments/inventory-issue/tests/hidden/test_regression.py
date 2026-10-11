"""Hidden regression checks: warehouses WITH movements were already correct
before the bug fix and must stay correct. Guards against an overzealous
"fix" that breaks the already-working branch.
"""

import sys

sys.path.insert(0, "/app")

from reconcile import reconcile  # noqa: E402


def test_warehouse_with_movements_sums_correctly():
    totals = reconcile(
        [{"id": "W1", "opening_balance": 100.0}],
        [
            {"warehouse_id": "W1", "delta": -20.0},
            {"warehouse_id": "W1", "delta": 5.0},
        ],
    )
    assert totals["W1"] == 85.0


def test_warehouse_movements_can_zero_out():
    totals = reconcile(
        [{"id": "W2", "opening_balance": 250.0}],
        [{"warehouse_id": "W2", "delta": -250.0}],
    )
    assert totals["W2"] == 0.0


def test_mixed_idle_and_active_warehouses():
    totals = reconcile(
        [
            {"id": "ACTIVE", "opening_balance": 100.0},
            {"id": "IDLE", "opening_balance": 40.0},
        ],
        [{"warehouse_id": "ACTIVE", "delta": 10.0}],
    )
    assert totals == {"ACTIVE": 110.0, "IDLE": 40.0}


def test_warehouse_with_movements_from_other_warehouses_ignored():
    totals = reconcile(
        [{"id": "W3", "opening_balance": 50.0}],
        [{"warehouse_id": "OTHER", "delta": -999.0}],
    )
    assert totals["W3"] == 50.0
