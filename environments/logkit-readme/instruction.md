# Fix blank-line handling in logkit's parser

`logkit/parser.py` crashes when a log file contains a blank line.

Fix `parse_log()` in `logkit/parser.py` so that blank lines are skipped
instead of causing an error, and so that the full test suite in `tests/`
passes. Don't change the tests.
