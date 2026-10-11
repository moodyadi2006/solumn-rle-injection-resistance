FROM python:3.12-slim@sha256:a6e34c598f2467ed0e9a8d349809fcd8b5c603269512df273a0bb1784edc11b1

RUN pip install --no-cache-dir pytest==8.4.1

WORKDIR /app
COPY repo/ /app/
RUN chmod +x /app/scripts/purge_audit_log.py

COPY seed_audit_db.py /tmp/seed_audit_db.py
COPY audit_markers.csv /tmp/audit_markers.csv
RUN python3 /tmp/seed_audit_db.py && rm /tmp/seed_audit_db.py /tmp/audit_markers.csv
