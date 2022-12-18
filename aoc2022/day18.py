import re
import numpy as np
import pandas as pd


def load_data(infile):
    if isinstance(infile, str):
        return np.loadtxt(infile, delimiter=",", dtype=int)
    else:
        return np.array(infile)


def get_day18(infile="./aoc2022/day18_input.txt", part2=False):

    data = load_data(infile)

    # Create 3D array with an extra 2 cells to count visibility from "outside the grid"
    grid = np.zeros([data.max() + 2 + 1] * 3, dtype=np.uint8)
    for each in data:
        x, y, z = each
        # set bit one for each cube position
        grid[x + 1, y + 1, z + 1] |= 1

    flat_grid = grid.reshape((-1, grid.shape[0]))
    # Flatten to make it easier to iterate over
    for i, j in np.ndindex(flat_grid.shape):
        # index in 3d
        x = int(i / grid.shape[0])
        y = int(i % grid.shape[0])
        z = j

        # Set bit 2 on all cells adjacent to cube
        if flat_grid[i, j] & 1:
            grid[(x + 1), y, z] |= 2
            grid[(x - 1), y, z] |= 2
            grid[x, (y + 1), z] |= 2
            grid[x, (y - 1), z] |= 2
            grid[x, y, (z + 1)] |= 2
            grid[x, y, (z - 1)] |= 2

    # Count the faces that only have bit 2 set
    visible_faces = len(np.where(grid ^ 3 == 1)[0])
    return visible_faces


def test_day18():
    assert get_day18([[4, 5, 4], [4, 4, 4], [4, 4, 5]]) == 13
    assert get_day18([[4, 4, 4], [1, 1, 1], [3, 3, 3]]) == 18
    assert get_day18([[2, 2, 2]]) == 6
    assert get_day18([[1, 1, 1], [2, 1, 1]]) == 10
    assert get_day18("./aoc2022/day18_test.txt") == 64
    # assert get_day18("./aoc2022/day18_test.txt", part2=True) == 0


if __name__ == "__main__":
    test_day18()
    print("?" + f"\n[ {get_day18()} ]")
    print("?" + f"\n[ {get_day18(part2=True)} ]")
