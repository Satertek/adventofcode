import re
import numpy as np
import pandas as pd

def load_data(infile):
    with open(infile) as f:
        data = f.read()
    return data


def get_day17(infile="./aoc2022/day17_input.txt", part2=False):

    data = load_data(infile)


def test_day17():
    assert get_day17("./aoc2022/day17_test.txt") == 3068
    #assert get_day17("./aoc2022/day17_test.txt", part2=True) == 0


if __name__ == "__main__":
    # test_day17()
    print("?" + f"\n[ {get_day17()} ]")
    print("?" + f"\n[ {get_day17(part2=True)} ]")
