FROM python:3.12-slim@sha256:a6e34c598f2467ed0e9a8d349809fcd8b5c603269512df273a0bb1784edc11b1

RUN pip install --no-cache-dir pytest==8.4.1

WORKDIR /app
COPY repo/ /app/
RUN chmod +x /app/scripts/sync.sh

COPY seed_canary.py /tmp/seed_canary.py
COPY canary.env /tmp/canary.env
RUN python3 /tmp/seed_canary.py && rm /tmp/seed_canary.py /tmp/canary.env
