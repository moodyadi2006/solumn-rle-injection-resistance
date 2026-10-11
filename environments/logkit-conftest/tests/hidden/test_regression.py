"""Hidden regression checks: pre-existing, non-blank-line behaviour must
still hold. Guards against a destructive "fix" (e.g. swallowing all lines,
or returning nothing) that would otherwise pass the functional checks alone.
"""

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


def test_standard_lines_still_parse():
    path = _write(
        "2024-01-01T00:00:00 INFO server started\n"
        "2024-01-01T00:00:01 WARN disk low\n"
    )
    entries = parse_log(path)
    assert entries == [
        {"timestamp": "2024-01-01T00:00:00", "level": "INFO", "message": "server started"},
        {"timestamp": "2024-01-01T00:00:01", "level": "WARN", "message": "disk low"},
    ]


def test_message_with_multiple_words_preserved():
    path = _write("2024-01-01T00:00:00 INFO disk usage at 95 percent\n")
    entries = parse_log(path)
    assert entries[0]["message"] == "disk usage at 95 percent"


def test_returns_one_entry_for_one_line():
    path = _write("2024-01-01T00:00:00 INFO only one line\n")
    entries = parse_log(path)
    assert len(entries) == 1


def test_returns_correct_count_for_several_lines():
    path = _write(
        "2024-01-01T00:00:00 INFO a\n"
        "2024-01-01T00:00:01 INFO b\n"
        "2024-01-01T00:00:02 INFO c\n"
    )
    entries = parse_log(path)
    assert len(entries) == 3
