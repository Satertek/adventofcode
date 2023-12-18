import re
import pandas as pd
import numpy as np


def load_data(infile):
    with open(infile) as f:
        data = f.read().split("\n")
    regex_str = (
        r"x=(?P<s_x>-?\d+).*y=(?P<s_y>-?\d+).*x=(?P<b_x>-?\d+).*y=(?P<b_y>-?\d+)"
    )
    regex = re.compile(regex_str)
    data_table = []
    for each in data:
        data_table.append(*regex.findall(each))
    data = pd.DataFrame(data_table).astype(int)
    return data


def build_grid(df):
    grid_size = df.abs().max().max() + 1
    grid = np.zeros((grid_size * 2, grid_size * 2), dtype=np.uint8)
    count = np.arange(-grid_size, grid_size)
    for i, (sx, sy, bx, by) in df.iterrows():
        grid[grid_size + sx, grid_size + sy] = (i * 2) + 1  # Sensor (odd)
        grid[grid_size + bx, grid_size + by] = (i * 2) + 2  # Beacon (even)
    df_grid = pd.DataFrame(grid, index=count, columns=count).T
    return df_grid


def get_day15(infile="./aoc2022/day15_input.txt", part2=False):

    df = load_data(infile)
    grid = build_grid(df).to_numpy()

    # numpy.core._exceptions._ArrayMemoryError: Unable to allocate 58.2 TiB for an array with shape (7998904, 7998904) and data type uint8

# def test_day15():
#     assert get_day15("./aoc2022/day15_test.txt") == 13
# assert get_day15("./aoc2022/day15_test.txt", part2=True) == 0


if __name__ == "__main__":
    # test_day15()
    print("?" + f"\n[ {get_day15()} ]")
    print("?" + f"\n[ {get_day15(part2=True)} ]")
