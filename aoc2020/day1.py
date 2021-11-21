import numpy as np

def get_day1(expenses, part2=False):
    for entry1 in expenses:
        for entry2 in expenses:            
            if not part2:
                if entry1+entry2 == 2020:
                    return entry1*entry2
            else:
                for entry3 in expenses:
                    if entry1+entry2+entry3 == 2020:
                        return entry1*entry2*entry3

expenses = np.loadtxt("./aoc2020/day1_input.txt", int)
print(f"Part 1: {get_day1(expenses)}")

print(f"Part 2: {get_day1(expenses, True)}")