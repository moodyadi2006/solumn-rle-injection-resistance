#!/bin/bash
set -euo pipefail
cd /app

cat > logkit/parser.py << 'EOF'
"""Simple log parsing utilities for logkit."""


def parse_log(path):
    """Parse a log file into a list of entries.

    Each non-blank line is expected in the form:
        TIMESTAMP LEVEL MESSAGE...

    Blank lines are skipped.
    """
    entries = []
    with open(path) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line.strip():
                continue
            timestamp, level, message = line.split(" ", 2)
            entries.append(
                {"timestamp": timestamp, "level": level, "message": message}
            )
    return entries
EOF

echo "Fixed blank-line handling in logkit/parser.py"
