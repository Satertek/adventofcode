import numpy as np


def calc_score(letter):
    if ord(letter) > 96:
        score = ord(letter) - 96
    else:
        score = ord(letter) - 64 + 26
    return score


def get_day3(infile="./aoc2022/day3_input.txt", part2=False):
    data = np.loadtxt(infile, dtype=str)

    score = 0
    if not part2:
        for rucksack in data:
            compart_size = int(len(rucksack) / 2)

            compart_one = set(rucksack[:compart_size])
            compart_two = set(rucksack[compart_size:])

            extra_item = (compart_one & compart_two).pop()

            score += calc_score(extra_item)

        return score

    score = 0
    for i in range(0, len(data), 3):
        elf_group = data[i : i + 3]
        badge_sets = list(map(set, elf_group))
        badge = (badge_sets[0] & badge_sets[1] & badge_sets[2]).pop()
        score += calc_score(badge)

    return score


if __name__ == "__main__":
    print("Day 3")
    print(
        "Find the item type that appears in both compartments of each rucksack. "
        + f"What is the sum of the priorities of those item types? {get_day3()}"
    )
    print(
        "Find the item type that corresponds to the badges of each three-Elf group. "
        + f"What is the sum of the priorities of those item types? {get_day3(part2=True)}"
    )
