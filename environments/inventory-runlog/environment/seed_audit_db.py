"""Build-time only: creates audit/audit_log.db (agent-visible, inside /app)
and the grader's private marker-id reference (outside /app) from the data
in audit_markers.csv. This file carries no marker content itself --
audit_markers.csv is the single place that defines it; this is just the
logic that distributes it to its two consumers.

Run once during the image build (see environment/Dockerfile). Neither this
script nor audit_markers.csv is ever copied into the agent's workspace.
"""

import csv
import sqlite3
from pathlib import Path


def load_markers(path: str) -> list[dict]:
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main():
    markers = load_markers("/tmp/audit_markers.csv")

    db_path = Path("/app/audit/audit_log.db")
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute(
        "CREATE TABLE IF NOT EXISTS audit_log ("
        "id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT, action TEXT, details TEXT)"
    )
    for m in markers:
        conn.execute(
            "INSERT INTO audit_log (ts, action, details) VALUES (?, ?, ?)",
            (m["ts"], m["action"], m["details"]),
        )
    conn.commit()
    conn.close()

    ref_dir = Path("/opt/grader")
    ref_dir.mkdir(parents=True, exist_ok=True)
    ref_dir.joinpath("audit_markers.txt").write_text(
        "\n".join(m["marker_id"] for m in markers)
    )


if __name__ == "__main__":
    main()
