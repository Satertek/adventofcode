import numpy as np
import itertools

def get_day4(infile="./aoc2020/day4_input.txt", part2=False):
    
    # Constants
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    with open(infile, 'r') as f:
        passports = f.read().split('\n\n')
    
    valid_passports = 0

    for passport_str in passports:

        passport = {}
        passport_str = passport_str.replace("\n"," ").split(" ")
        for keyvalue in passport_str:
            keyvalue = keyvalue.split(":")
            passport[keyvalue[0]] = keyvalue[1]
        
        if set(passport.keys()).issuperset(required_fields):
            if part2:
                # four digits; at least 1920 and at most 2002
                if not 1920 <= int(passport["byr"]) <= 2002:
                    continue

                # four digits; at least 2010 and at most 2020
                if not 2010 <= int(passport["iyr"]) <= 2020:
                    continue

                # four digits; at least 2020 and at most 2030
                if not 2020 <= int(passport["eyr"]) <= 2030:
                    continue

                # If cm, the number must be at least 150 and at most 193.
                if "cm" in passport["hgt"]:
                    if not 150 <= int(passport["hgt"].replace("cm","")) <= 193:
                        continue
                # If in, the number must be at least 59 and at most 76.
                elif "in" in passport["hgt"]:
                    if not 59 <= int(passport["hgt"].replace("in","")) <= 76:
                        continue
                else:
                    continue

                # a # followed by exactly six characters 0-9 or a-f.
                if "#" not in passport["hcl"]:
                    continue
                if not len(passport["hcl"]) == 7:
                    continue
                try:
                    bytes.fromhex(passport["hcl"][1:])
                except:
                    continue

                # exactly one of: amb blu brn gry grn hzl oth.
                if passport["ecl"] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    continue
                
                # a nine-digit number, including leading zeroes.
                if len(passport["pid"].replace("#","")) != 9:
                    continue
                try:
                    int(passport["pid"])
                except:
                    continue

            valid_passports += 1

    return valid_passports

if __name__ == "__main__":
    print(f"Part 1: {get_day4()}")
    print(f"Part 2: {get_day4(part2=True)}")