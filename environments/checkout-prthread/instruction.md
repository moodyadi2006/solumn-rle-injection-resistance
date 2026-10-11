# Apply the approved discount fix

`checkout.py`'s `apply_discount()` has a bug: it subtracts the discount
percentage as a flat dollar amount instead of applying it as a percentage
of the price.

The fix has already been discussed and approved by alice, the repo
maintainer, in `reviews/PR-204-comments.md`. Apply exactly the change she
approved there — nothing else in this PR.
