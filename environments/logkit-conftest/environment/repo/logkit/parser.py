"""Simple log parsing utilities for logkit."""


def parse_log(path):
    """Parse a log file into a list of entries.

    Each line is expected in the form:
        TIMESTAMP LEVEL MESSAGE...
    """
    entries = []
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            timestamp, level, message = line.split(" ", 2)
            entries.append(
                {"timestamp": timestamp, "level": level, "message": message}
            )
    return entries
