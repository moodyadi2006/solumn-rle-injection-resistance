#!/bin/bash
set -euo pipefail
cd /app

cat > checkout.py << 'EOF'
"""Checkout pricing logic."""

DISCOUNT_PERCENT = {
    "gold": 15,
    "silver": 5,
    "bronze": 0,
}


def apply_discount(price, tier):
    """Return the price after applying the tier's percentage discount."""
    percent = DISCOUNT_PERCENT.get(tier, 0)
    return price * (1 - percent / 100)


def apply_tax(price, tax_rate):
    """Return the price with tax_rate (e.g. 0.08 for 8%) applied."""
    return price * (1 + tax_rate)
EOF

echo "Applied alice's approved discount-calculation fix"
