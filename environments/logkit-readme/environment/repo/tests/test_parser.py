from pathlib import Path

from logkit.parser import parse_log


def _write(tmp_path, name, content):
    p = tmp_path / name
    p.write_text(content)
    return p


def test_parses_standard_lines(tmp_path):
    p = _write(
        tmp_path,
        "a.log",
        "2024-01-01T00:00:00 INFO server started\n"
        "2024-01-01T00:00:01 WARN disk low\n",
    )
    entries = parse_log(p)
    assert entries == [
        {"timestamp": "2024-01-01T00:00:00", "level": "INFO", "message": "server started"},
        {"timestamp": "2024-01-01T00:00:01", "level": "WARN", "message": "disk low"},
    ]


def test_handles_blank_lines(tmp_path):
    p = _write(
        tmp_path,
        "b.log",
        "2024-01-01T00:00:00 INFO server started\n"
        "\n"
        "2024-01-01T00:00:01 WARN disk low\n",
    )
    entries = parse_log(p)
    assert entries == [
        {"timestamp": "2024-01-01T00:00:00", "level": "INFO", "message": "server started"},
        {"timestamp": "2024-01-01T00:00:01", "level": "WARN", "message": "disk low"},
    ]
