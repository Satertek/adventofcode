import numpy as np

def get_day5(infile="./aoc2020/day5_input.txt", part2=False):
    with open(infile, 'r') as f:
        data = f.read().split("\n")
        seats = []
        for each in data:
            seats.append(
                [int(each[0:7].replace("F","0").replace("B","1"), 2), 
                 int(each[7: ].replace("L","0").replace("R","1"), 2)
                ])
    
    seat_id = []
    for row, column in seats:
        seat_id.append(
            row * 8 + column
        )
    if not part2:
        return np.max(seat_id)
    else:
        missing_values = set(np.arange(0,np.max(seat_id))).difference(set(seat_id))
        # Return seat number that is between two taken seats
        for each in missing_values:
            if each - 1 in seat_id and each + 1 in seat_id:
                return each

if __name__ == "__main__":
    print(f"Part 1: {get_day5()}")
    print(f"Part 2: {get_day5(part2=True)}")