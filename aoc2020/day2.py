import numpy as np

def get_day2(infile="./aoc2020/day2_input.txt", part2=False):
    valid_passwords = 0

    passwords = np.loadtxt(infile, str, delimiter=" ")

    for line in passwords:
        min_qty, max_qty = list(map(int,line[0].split("-")))
        letter = line[1].replace(":","")
        password = line[2]

        if not part2:
            qty = password.count(letter)
            if qty >= min_qty and qty <= max_qty:
                valid_passwords += 1
        else:
            if (password[min_qty-1] + password[max_qty-1]).count(letter) == 1:
                valid_passwords += 1
    
    return valid_passwords

if __name__ == "__main__":
    print(f"Part 1: {get_day2()}")
    print(f"Part 2: {get_day2(part2=True)}")