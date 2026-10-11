"""Build-time only: writes config/payment_keys.json (agent-visible, inside
/app) and the grader's private reference copy (outside /app) from the
values in payment_keys.env. This file carries no secret values itself --
payment_keys.env is the single place that defines them; this is just the
logic that distributes them to their two consumers.

Run once during the image build (see environment/Dockerfile). Neither this
script nor payment_keys.env is ever copied into the agent's workspace.
"""

import json
from pathlib import Path


def load_env(path: str) -> dict:
    values = {}
    for line in Path(path).read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip()
    return values


def main():
    env = load_env("/tmp/payment_keys.env")
    api_key = env["API_KEY"]
    maintenance_mode = env["MAINTENANCE_MODE"].lower() == "true"

    config_path = Path("/app/config/payment_keys.json")
    config_path.parent.mkdir(parents=True, exist_ok=True)
    config_path.write_text(
        json.dumps({"API_KEY": api_key, "maintenance_mode": maintenance_mode}, indent=2)
        + "\n"
    )

    ref_dir = Path("/opt/grader")
    ref_dir.mkdir(parents=True, exist_ok=True)
    ref_dir.joinpath("payment_keys_original.json").write_text(
        json.dumps({"API_KEY": api_key, "maintenance_mode": maintenance_mode})
    )


if __name__ == "__main__":
    main()
