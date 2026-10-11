"""Clears the audit log. Destructive -- removes all historical audit rows."""

import sqlite3
from pathlib import Path

AUDIT_DB = Path(__file__).parent.parent / "audit" / "audit_log.db"


def main():
    conn = sqlite3.connect(AUDIT_DB)
    conn.execute("DELETE FROM audit_log")
    conn.commit()
    conn.close()
    print("audit_log cleared")


if __name__ == "__main__":
    main()
