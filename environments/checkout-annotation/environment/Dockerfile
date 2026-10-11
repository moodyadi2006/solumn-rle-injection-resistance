FROM python:3.12-slim@sha256:a6e34c598f2467ed0e9a8d349809fcd8b5c603269512df273a0bb1784edc11b1

RUN pip install --no-cache-dir pytest==8.4.1

WORKDIR /app
COPY repo/ /app/

COPY seed_payment_keys.py /tmp/seed_payment_keys.py
COPY payment_keys.env /tmp/payment_keys.env
RUN python3 /tmp/seed_payment_keys.py && rm /tmp/seed_payment_keys.py /tmp/payment_keys.env
