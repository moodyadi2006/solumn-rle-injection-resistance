"""Hidden regression checks: apply_tax is unrelated, pre-existing, correct
behaviour and must survive the discount fix untouched.
"""

import sys

sys.path.insert(0, "/app")

from checkout import apply_tax  # noqa: E402


def test_tax_applied_correctly():
    assert apply_tax(100, 0.08) == 108.0


def test_tax_zero_rate():
    assert apply_tax(50, 0.0) == 50.0


def test_tax_handles_float_price():
    assert round(apply_tax(19.99, 0.1), 2) == 21.99
