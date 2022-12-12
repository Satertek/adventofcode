import re
import numpy as np
import pandas as pd


def get_day11(infile="./aoc2022/day11_input.txt", part2=False):
    with open(infile) as f:
        data = f.read().split("\n\n")

    # Parse input data
    match_str = (
        r"Monkey (?P<monkey>\d+):\n.*items: (?P<items>(\d+(, )?)+)\n.*= (?P<func>.*)\n.*"
        + r"by (?P<test>\d+)\n.*monkey (?P<if_true>\d+)\n.*monkey (?P<if_false>\d+)"
    )
    regex = re.compile(match_str)
    monkey_dict = {}
    for each in data:
        d = regex.match(each).groupdict()
        monkey_dict[d["monkey"]] = d.copy()

    # Pre-process and add columns
    largest_divisor = 0
    for k, d in monkey_dict.items():
        d["items"] = list(np.fromstring(d["items"], sep=",", dtype=int))
        d["items_checked"] = 0
    # Get the least common multiple of divisors so we can cap our item values
    lcm = np.lcm.reduce(
        pd.DataFrame(monkey_dict).transpose()["test"].values.astype(int)
    )

    # Perform each round of checks
    for round in range((10000 if part2 else 20)):
        for k, d in monkey_dict.items():
            for old in d["items"]:
                d["items_checked"] += 1
                new = np.floor(np.floor(eval(d["func"])) / (1 if part2 else 3))
                monkey_target = str(
                    int(d["if_true"])
                    if (new % int(d["test"]) == 0)
                    else int(d["if_false"])
                )
                # Reduce item to below 2*least common multiple
                if new > lcm:
                    new = (new % lcm) + lcm
                # send item to target monkey
                monkey_dict[monkey_target]["items"].append(new)
            # clear monkey item list after everything checked
            d["items"] = []

    df = pd.DataFrame(monkey_dict).transpose()

    # return product of 2 largest values
    return df["items_checked"].sort_values()[-2:].product()


def test_day11():
    assert get_day11("./aoc2022/day11_test.txt") == 10605
    assert get_day11("./aoc2022/day11_test.txt", part2=True) == 2713310158


if __name__ == "__main__":
    test_day11()
    print(
        "What is the level of monkey business after 20 rounds?" + f"\n[ {get_day11()} ]"
    )
    print(
        "What is the level of monkey business after 10000 rounds?"
        + f"\n[ {get_day11(part2=True)} ]"
    )
