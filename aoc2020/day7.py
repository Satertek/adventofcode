import numpy as np

def find_bag(d, k, find="shiny gold"):
    if find in d[k]:
        return True
    for each in d[k]:
        found = find_bag(d, each, find)
        if found:
            return True
    return False

def count_bags(d, b, find="shiny gold"):
    count = 0
    for i, each in enumerate(d[find]):
        count += b[find][i] * (count_bags(d,b,each)+1)
    return count

def get_day7(infile="./aoc2020/day7_input.txt", part2=None):

    with open(infile, 'r') as f:
        rules = f.read().split("\n")

    for i, _ in enumerate(rules):
        rules[i] = rules[i].split("contain")
    rules_dict = {}
    for k,v in rules:
        new_key = k.replace("bags","").replace("bag","").strip()
        if "other" in v:
            rules_dict[new_key] = []
        else:
            rules_dict[new_key] = (v.replace(".","")
                                    .replace("bags","")
                                    .replace("bag","")
                                    .split(","))
    bag_counts = {}
    for k,v in rules_dict.items():
        #remove count and whitespace from keys
        bag_counts[k] = []
        for i,j in enumerate(rules_dict[k]):
            bag_counts[k].append(int(j[1:3]))
            rules_dict[k][i] = j[3:].strip()
    
    valid_colors = {}
    valid_count = 0
    valid_count2 = 0
    for key in rules_dict.keys():
        valid_colors[key] = find_bag(rules_dict, key)
        if valid_colors[key]:
            if part2:
                valid_count2+=0
            valid_count+=1

    valid_count2 = count_bags(rules_dict, bag_counts)

    return valid_count, valid_count2

if __name__ == "__main__":
    part1, part2 = get_day7()
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")