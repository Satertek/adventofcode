import re
import numpy as np
import pandas as pd


def position_at_value(data, value):
    x, y = (data == value).nonzero()
    return [x[0], y[0]]


def get_day12(infile="./aoc2022/day12_input.txt", part2=False):
    with open(infile) as f:
        data = np.array(list(list(map(ord, x.strip())) for x in f.readlines()))
        data -= ord("a")

    start = position_at_value(data, -14)
    end = position_at_value(data, -28)

    current_height = 0
    while True:
        search_area = [
            sum(start, [1, 0]),
            sum(start, [0, 1]),
            sum(start, [-1, 0]),
            sum(start, [0, -1]),
        ]
        print(search_area)
        for x, y in search_area:
            if x < 0 or y < 0:
                search_area = [[x, y] for [x, y] in search_area if not (x == 0).all()]
            if np.abs(data[x, y] - current_height) > 1:
                search_area.remove((x, y))
        break


# def test_day12():
#     assert get_day12("./aoc2022/day12_test.txt") == 10605
#     assert get_day12("./aoc2022/day12_test.txt", part2=True) == 2713310158


if __name__ == "__main__":
    # test_day12()
    print(
        "What is the fewest steps required to move from your current position to the location that should get the best signal?"
        + f"\n[ {get_day12()} ]"
    )
    print(
        "What is the fewest steps required to move from your current position to the location that should get the best signal?"
        + f"\n[ {get_day12(part2=True)} ]"
    )
