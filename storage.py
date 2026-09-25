import json


def get_json(filename: str) -> list[dict]:
    with open(filename, "r") as json_read:
        return json.load(json_read)

