import json
from pathlib import Path

DATA_PATH = Path("data/log.json")

def save_log(date_str, entry):
    if DATA_PATH.exists():
        with open(DATA_PATH, "r") as f:
            data = json.load(f)
    else:
        data = {}

    data[date_str] = entry

    with open(DATA_PATH, "w") as f:
        json.dump(data, f, indent=2)
