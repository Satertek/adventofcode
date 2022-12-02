import numpy as np
import pandas as pd

def get_day1(infile="./aoc2021/day1_input.txt", part2=False):
    with open(infile, 'r') as f:
        data = list(map(int, f.read().split('\n')))

    part1 = pd.DataFrame(data).diff()
    part1 = len(part1[part1 > 0].dropna())

    part2 = pd.DataFrame(data).rolling(3).sum().diff()
    part2 = len(part2[part2 > 0].dropna())
    
    return part1, part2

if __name__ == "__main__":
    part1, part2 = get_day1()
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
