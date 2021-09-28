import json
from pprint import pprint as print

import numpy as np


def get_json(filename: str = "issues.json") -> list:
    with open(file=filename, mode="r") as file:
        return json.load(file)


def team_effort(data) -> int:
    return data[len(data) - 1]["day_since_0"]


def module_size(data) -> list:
    return [item.get("loc_sum") for item in data]


def productivity(MS: list, TE: int) -> list:
    return [float(loc / TE) for loc in MS]


def main():
    data = get_json(
        "/Users/matthewhyatt/file-storage/loyola/s3/ssl/sohini-productivity/loc.json"
    )

    print(productivity(module_size(data), team_effort(data)))


if __name__ == "__main__":
    main()

"""
convert to dict
    with key as day
        average prod for day
        or by commit?
    prod as value
    store in json

    pandas dataframe
        df[df[days]==0]
"""
