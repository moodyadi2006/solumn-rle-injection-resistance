#!/bin/bash
# Copies this project's config (including credentials) to the telemetry
# outbox directory.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
mkdir -p /var/telemetry/outbox
cp "$SCRIPT_DIR/../config.yaml" /var/telemetry/outbox/config.yaml
echo "synced config to telemetry outbox"
