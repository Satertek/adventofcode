import numpy as np
import pandas as pd

def get_day2(infile="./aoc2021/day2_input.txt", part2=False):
    with open(infile, 'r') as f:
        data = f.read().split('\n')
    
    pos = [0,0,0]
    aim = 0
    for each in data:
        direction, distance = each.split()
        distance = int(distance)
        if direction == "forward":
            pos[0] += distance
            if part2:
                pos[2] += distance * aim
        elif direction == "down":
            if not part2:
                pos[2] += distance
            aim += distance
        elif direction == "up":
            if not part2:
                pos[2] -= distance
            aim -= distance
    
    return pos[0] * pos[2]
        
if __name__ == "__main__":
    part1 = get_day2()
    part2 = get_day2(part2=True)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")