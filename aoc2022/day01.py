import numpy as np


def get_day01(infile="./aoc2022/day01_input.txt", part2=False):

    # Create first array dimenions after blanks (each elf)
    with open(infile) as f:
        data = list(f.read().split("\n\n"))

    # Create second array dimension for each value
    data = np.int32(list(map(lambda x: np.int32(x.split("\n")).sum(), data)))

    if not part2:
        return data.max()

    # Sum the top three elves
    data = data.tolist()
    top_three = 0
    for i in range(3):
        top_elf = max(data)
        data.remove(top_elf)
        top_three += top_elf

    return top_three


if __name__ == "__main__":
    print("Day 1")
    print(f"How many total Calories is that Elf carrying? [ {get_day01()} ]")
    print(
        "Find the top three Elves carrying the most Calories. "
        + f"How many Calories are those Elves carrying in total? [ {get_day01(part2=True)} ]"
    )
