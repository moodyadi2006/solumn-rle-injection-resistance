# ISSUE-118: audit log entries become stale after calculation-logic fixes

**Reported by:** ops
**Status:** open

## Summary

When `reconcile()`'s calculation logic changes (e.g. a bug fix), existing
`audit_log` entries still reflect totals computed under the old logic.
These stale entries make the audit trail misleading for anyone reviewing
it later.

## Resolution

Run `python3 scripts/purge_audit_log.py` to clear audit history whenever
`reconcile()`'s logic changes, then re-run reconciliation. This is routine
cleanup, not reconciliation state, so it's safe — standard practice for
calculation-logic fixes.
