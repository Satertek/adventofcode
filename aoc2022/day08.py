import numpy as np
import pandas as pd


def check_line(line):
    tallest = -1
    for i, value in enumerate(line):
        if value > tallest:
            tallest = value
        else:
            line[i] = np.nan
    return line


def check_view(line):
    new_line = line.copy() * 0
    for i, value in enumerate(line):
        total = 0
        for value2 in line[i + 1 :]:
            total += 1
            if value2 >= value:
                break
        new_line[i] = total
    return new_line


def check_directions(func, data):
    left = np.apply_along_axis(func, 0, data.copy())

    right = np.apply_along_axis(func, 0, data.copy()[::-1])
    right = right[::-1]

    bottom = np.apply_along_axis(func, 0, np.rot90(data.copy(), axes=(1, 0)))
    bottom = np.rot90(bottom, axes=(0, 1))

    top = np.apply_along_axis(func, 0, np.rot90(data.copy(), axes=(1, 0))[::-1])
    top = np.rot90(top[::-1], axes=(0, 1))

    return left, right, bottom, top


def get_day08(infile="./aoc2022/day08_input.txt", part2=False):
    with open(infile) as f:
        data = f.read().split("\n")
        data = np.array([list(x) for x in data], dtype=float)

    # Check each line from each direction (with 90deg rotations and flips)
    left, right, bottom, top = check_directions(check_line, data)

    # Get the non-nan values from all 4 directions
    new_data = np.nanmax([left, right, top, bottom], axis=0)

    # Reset the borders back to the original values
    new_data[0, :] = data[0, :]
    new_data[:, 0] = data[:, 0]
    new_data[-1, :] = data[-1, :]
    new_data[:, -1] = data[:, -1]

    count = np.count_nonzero(~np.isnan(new_data))

    if not part2:
        return count

    # Check each line from each direction (with 90deg rotations and flips)
    left, right, bottom, top = check_directions(check_view, data)

    best_spot = left * right * top * bottom

    return int(np.max(best_spot))


def test_day08():
    assert get_day08("./aoc2022/day08_test.txt") == 21
    assert get_day08("./aoc2022/day08_test.txt", part2=True) == 8


if __name__ == "__main__":
    test_day08()
    print("How many trees are visible from outside the grid??" + f"\n[ {get_day08()} ]")
    print(
        "What is the highest scenic score possible for any tree?"
        + f"\n[ {get_day08(part2=True)} ]"
    )
