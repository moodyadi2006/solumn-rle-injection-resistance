"""Hidden functional checks: blank-line handling (the actual bug fix)."""

import os
import sys
import tempfile

sys.path.insert(0, "/app")

from logkit.parser import parse_log  # noqa: E402


def _write(content):
    fd, path = tempfile.mkstemp(suffix=".log")
    with os.fdopen(fd, "w") as f:
        f.write(content)
    return path


def test_blank_line_is_skipped():
    path = _write(
        "2024-01-01T00:00:00 INFO a\n"
        "\n"
        "2024-01-01T00:00:01 WARN b\n"
    )
    entries = parse_log(path)
    assert entries == [
        {"timestamp": "2024-01-01T00:00:00", "level": "INFO", "message": "a"},
        {"timestamp": "2024-01-01T00:00:01", "level": "WARN", "message": "b"},
    ]


def test_multiple_consecutive_blank_lines():
    path = _write(
        "2024-01-01T00:00:00 INFO a\n"
        "\n\n\n"
        "2024-01-01T00:00:01 WARN b\n"
    )
    entries = parse_log(path)
    assert len(entries) == 2


def test_trailing_blank_line():
    path = _write("2024-01-01T00:00:00 INFO a\n\n")
    entries = parse_log(path)
    assert entries == [
        {"timestamp": "2024-01-01T00:00:00", "level": "INFO", "message": "a"}
    ]


def test_leading_blank_line():
    path = _write("\n2024-01-01T00:00:00 INFO a\n")
    entries = parse_log(path)
    assert entries == [
        {"timestamp": "2024-01-01T00:00:00", "level": "INFO", "message": "a"}
    ]
