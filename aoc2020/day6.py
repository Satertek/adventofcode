def get_day6(infile="./aoc2020/day6_input.txt", part2=False):

    with open(infile, 'r') as f:
        groups = f.read().split("\n\n")
    
    yes_questions = 0
    if not part2:
        for i, _ in enumerate(groups):
            groups[i] = set(groups[i].replace("\n",""))
            yes_questions += len(groups[i])
    else:
        for i, _ in enumerate(groups):
            groups[i] = groups[i].split("\n")
            for x, _ in enumerate(groups[i]):
                if x == 0:
                    common_set = set(groups[i][0])
                else:
                    common_set = common_set.intersection(set(groups[i][x]))
            yes_questions += len(common_set)
    return yes_questions

if __name__ == "__main__":
    print(f"Part 1: {get_day6()}")
    print(f"Part 2: {get_day6(part2=True)}")