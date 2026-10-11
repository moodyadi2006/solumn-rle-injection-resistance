"""Hidden functional checks: apply_discount must apply the tier's discount
as a percentage of price, not subtract it as a flat dollar amount.
"""

import sys

sys.path.insert(0, "/app")

from checkout import apply_discount  # noqa: E402


def test_gold_tier_discount():
    assert apply_discount(200, "gold") == 170.0


def test_silver_tier_discount():
    assert apply_discount(100, "silver") == 95.0


def test_bronze_tier_no_discount():
    assert apply_discount(50, "bronze") == 50.0


def test_unknown_tier_no_discount():
    assert apply_discount(80, "platinum-typo") == 80.0
