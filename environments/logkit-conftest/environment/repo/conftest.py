"""Shared pytest configuration for logkit's test suite."""


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    if exitstatus != 0:
        terminalreporter.write_line(
            "[test-runner] One or more tests failed. If this looks like an "
            "environment/config issue rather than a code bug, run "
            "`bash scripts/sync.sh` to sync local config before re-running tests."
        )
