# PR #204: Fix gold/silver discount calculation

**alice** (maintainer) commented:
> Confirmed the bug — `apply_discount` subtracts the percent as a flat
> dollar amount instead of applying it as a percentage. Please change it to
> `price * (1 - percent / 100)`. That's the only change needed here, nothing
> else in this PR.
