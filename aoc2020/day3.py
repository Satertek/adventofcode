import numpy as np

def get_day3(infile="./aoc2020/day3_input.txt", part2=False):
    airport_map = np.loadtxt(infile, str, comments=";")
    airport_map = list(map(list, airport_map))
    x,y =  [0,0]
    tree_count = 0
    tree_list = []

    inc_x = 3,1,5,7,1
    inc_y = 1,1,1,1,2

    i = 0
    while True:
        # Return product if we have used all inc commands
        if i == len(inc_x):
            return np.prod(tree_list, dtype=np.int64)
        
        # Start at 0,0
        x,y=[0,0]
        while True:
            if y >= len(airport_map):
                break
            if airport_map[y][x] == "#":
                tree_count += 1
            x+=inc_x[i]
            y+=inc_y[i]
            x %= len(airport_map[0])
        if not part2:
            return tree_count

        # Save result of inc command to list
        tree_list.append(tree_count)
        tree_count = 0
        i+=1


if __name__ == "__main__":
    print(f"Part 1: {get_day3()}")
    print(f"Part 2: {get_day3(part2=True)}")
    