import numpy as np
import pandas as pd


def get_tail_positions(input_positions):
    pos_h = np.array([0, 0], dtype=float)
    pos_t = np.array([0, 0], dtype=float)
    unique_pos = set([tuple(pos_t)])
    all_pos = []

    for pos_h in input_positions:
        tail_distance = np.linalg.norm(pos_h - pos_t)
        if tail_distance > np.sqrt(2):
            pos_t += np.sign(pos_h - pos_t) * np.ceil(np.abs((pos_h - pos_t) / 2))
            unique_pos.add(tuple(pos_t))
            all_pos.append(tuple(pos_t))

    return all_pos, unique_pos


def process_input(data):
    pos = np.array([0, 0], dtype=float)
    all_pos = []
    for direction, steps in data:
        for _ in range(int(steps)):
            match direction:
                case "R":
                    pos += [1, 0]
                case "L":
                    pos += [-1, 0]
                case "U":
                    pos += [0, 1]
                case "D":
                    pos += [0, -1]
            all_pos.append(tuple(pos))

    return all_pos


def get_day09(infile="./aoc2022/day09_input.txt", part2=False):
    data = np.loadtxt(infile, delimiter=" ", dtype=str)
    all_pos = process_input(data)  # initial position list derived from input

    for _ in range(9):
        all_pos, unique_pos = get_tail_positions(all_pos)
        if not part2:
            # Return tail #1
            return len(unique_pos)
    
    # Return tail #9
    return len(unique_pos)


def test_day09():
    assert get_day09("./aoc2022/day09_test.txt") == 13
    assert get_day09("./aoc2022/day09_test2.txt", part2=True) == 36


if __name__ == "__main__":
    test_day09()
    print(
        "How many positions does the tail of the rope visit at least once?"
        + f"\n[ {get_day09()} ]"
    )
    print(
        "How many positions does (all 10 knots of) the tail of the rope visit at least once?"
        + f"\n[ {get_day09(part2=True)} ]"
    )
