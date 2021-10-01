import argparse
import json
from pprint import pprint as print

import numpy as np


def get_args():
    ap = argparse.ArgumentParser(
        prog="SSL Metrics Git Productivity",
        usage="Calculates productivity measure of a git project.",
    )
    ap.add_argument("--jsonfile", "-j", required=True, type=open, help="...")

    args = ap.parse_args()
    return args


def get_data(filename: str = "issues.json") -> list:
    with open(file=filename, mode="r") as file:
        return json.load(file)


def team_effort(data) -> int:
    return data[len(data) - 1]["day_since_0"]


def module_size(data) -> list:
    return [commit["loc_sum"] for commit in data]


def productivity(MS: list, TE: int) -> list:
    return [float(loc / TE) for loc in MS]


def update(filename: str, data: list, name: str, field: list):
    "adds the given field as key value pairs to json file"

    for commit, item in zip(data, field):
        commit[name] = item
    with open(file=filename, mode="w") as file:
        json.dump(data, file)


def main():

    args = get_args()
    jsonfile = args.jsonfile.name

    data = get_data(jsonfile)
    prod = productivity(module_size(data), team_effort(data))

    update(jsonfile, data, "productivity", prod)


if __name__ == "__main__":
    main()
