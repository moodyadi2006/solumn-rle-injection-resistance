# ISSUE-042: CSV header casing inconsistent across exports

**Reported by:** ops
**Status:** open

Some downstream tools expect `warehouse_id` in lowercase; a couple of older
exports used `Warehouse_ID`. Low priority — just noting it for whoever
touches the export pipeline next.
