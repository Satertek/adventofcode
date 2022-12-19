import re
import numpy as np
import pandas as pd
from scipy import ndimage


def load_data(infile):
    if isinstance(infile, str):
        return np.loadtxt(infile, delimiter=",", dtype=int)
    else:
        return np.array(infile)


def increment_faces(grid, x, y, z):
    if grid[x, y, z] & 1 == 1:
        return
    grid[x, y, z] = (grid[x, y, z] + 1) << 1


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

        # Shift a bit every time we count the empty space
        if flat_grid[i, j] & 1:
            increment_faces(grid, (x + 1), y, z)
            increment_faces(grid, (x - 1), y, z)
            increment_faces(grid, x, (y + 1), z)
            increment_faces(grid, x, (y - 1), z)
            increment_faces(grid, x, y, (z + 1))
            increment_faces(grid, x, y, (z - 1))

    # Replace all values in grid with number of faces visible at that location
    grid = np.vectorize(lambda x: bin(x).count("1"))(grid >> 1)

    if part2:
        # Remove bubbles
        grid *= (
            ~ndimage.binary_erosion(
                (ndimage.binary_fill_holes(grid)).astype(int), iterations=2
            )
        ).astype(int)

    visible_faces = grid.sum()

    return visible_faces


def test_day18():
    assert get_day18([[1, 1, 1], [2, 1, 1]]) == 10
    assert get_day18("./aoc2022/day18_test.txt") == 64
    assert get_day18("./aoc2022/day18_test.txt", part2=True) == 58


if __name__ == "__main__":
    test_day18()
    print(
        "What is the surface area of your scanned lava droplet?"
        + f"\n[ {get_day18()} ]"
    )
    print(
        "What is the surface area of your scanned lava droplet (excluding air bubbles)?"
        + f"\n[ {get_day18(part2=True)} ]"
    )
