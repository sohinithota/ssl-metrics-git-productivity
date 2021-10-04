from argparse import ArgumentParser, Namespace
from os import path

import matplotlib.pyplot as plt
import pandas
from matplotlib.figure import Figure
from pandas import DataFrame


def get_argparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        prog="Convert Output",
        usage="This program converts a JSON file into various different formats.",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="The input data file that will be read to create the graphs",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output",
        help="The filename to output the graph to",
        type=str,
        required=True,
    )
    return parser.parse_args()


# prod_sum over time where time is spaced by day
def plot(df: DataFrame, filename: str) -> None:
    figure: Figure = plt.figure()
    plt.ylabel("prod")
    plt.xlabel("day_since_0")
    plt.title("Daily Productivity Sum Over Time")

    unique_days = list(set(df['day_since_0']))
    print(unique_days)
    prod_sum = [0 for day in unique_days]

    for day in unique_days:
        for i in range(len(df)):
            if df.iloc[i]['day_since_0'] == day:
                prod_sum[unique_days.index(day)] += abs(df.iloc[i]['productivity'])

    print(prod_sum)

    plt.bar(unique_days, prod_sum)
    # plt.scatter(df['day_since_0'], df['productivity'])
    figure.savefig(filename)


def main():
    args:Namespace = get_argparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)

    df:DataFrame = pandas.read_json(args.input)
    print(df)

    plot(df, filename=args.output)


if __name__ == "__main__":
    main()
