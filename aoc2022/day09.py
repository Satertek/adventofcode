import numpy as np
import pandas as pd


def get_day09(infile="./aoc2022/day09_input.txt", part2=False):
    data = np.loadtxt(infile, delimiter=" ", dtype=str)

    pos_h = np.array([0, 0], dtype=float)
    pos_t = np.array([0, 0], dtype=float)

    tail_positions = set((0, 0))
    for direction, steps in data:
        for _ in range(int(steps)):
            # print(f"{direction}1")
            match direction:
                case "R":
                    pos_h += [1, 0]
                case "L":
                    pos_h += [-1, 0]
                case "U":
                    pos_h += [0, 1]
                case "D":
                    pos_h += [0, -1]
            tail_distance = np.linalg.norm(pos_h - pos_t)
            if tail_distance > np.sqrt(2):
                tail_positions.add(tuple(pos_t))
                pos_t += np.sign(pos_h - pos_t) * np.ceil(np.abs((pos_h - pos_t) / 2))

    return len(tail_positions)


def test_day09():
    assert get_day09("./aoc2022/day09_test.txt") == 13
    # assert get_day09("./aoc2022/day09_test.txt", part2=True) == 8


if __name__ == "__main__":
    test_day09()
    print(
        "How many positions does the tail of the rope visit at least once?"
        + f"\n[ {get_day09()} ]"
    )
    # print(
    #    "?"
    #    + f"\n[ {get_day09(part2=True)} ]"
    # )
