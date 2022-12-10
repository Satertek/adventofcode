import numpy as np


def get_day4(infile="./aoc2022/day4_input.txt", part2=False):
    with open(infile) as f:
        data = np.loadtxt((x.replace("-", ",") for x in f), delimiter=",", dtype=int)
    overlap_count = 0
    complete_count = 0
    for pair in data:

        elf_one = set(range(pair[0], pair[1] + 1))
        elf_two = set(range(pair[2], pair[3] + 1))

        overlaps = list(elf_one & elf_two)

        if len(overlaps) in (len(elf_one), len(elf_two)):
            complete_count += 1
        if len(overlaps):
            overlap_count += 1
    if not part2:
        return complete_count
    return overlap_count


def test_day04():
    assert get_day4("./aoc2022/day4_test.txt") == 2
    assert get_day4("./aoc2022/day4_test.txt", part2=True) == 4


if __name__ == "__main__":
    print("Day 4")
    test_day04()
    print(
        "In how many assignment pairs does one range fully contain the other?"
        + f"\n[ {get_day4()} ]"
    )
    print(
        "In how many assignment pairs do the ranges overlap?"
        + f"\n[ {get_day4(part2=True)} ]"
    )
