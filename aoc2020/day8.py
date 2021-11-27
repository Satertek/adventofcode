import copy

def run_program(commands, part1=False):
    
    acc = 0
    i=0
    instruction_list = []
    while True:
        if i == len(commands):
            print(f"Successful exit at line {i+1}")
            break
        if i > len(commands):
            print("BUFFER OVERFLOW")
            return False
        if i in instruction_list:
            if part1:
                break
            else:
                return False
        instruction_list.append(i)
        k,v = commands[i]
        if k == "acc":
            acc+=v
        if k == "jmp":
            i+=v
        else:
            i+=1
    
    return acc

def get_day8(infile="./aoc2020/day8_input.txt"):

    with open(infile, 'r') as f:
        commands = f.read().split("\n")
    for i, _ in enumerate(commands):
        commands[i] = commands[i].split(" ")
        commands[i][1] = int(commands[i][1])

    part1 = run_program(commands, part1=True)

    # PART 2
    part2 = False
    for i,(k,v) in enumerate(commands):
        if k in ("nop","jmp"):
            tmp = copy.deepcopy(commands)
            tmp[i][0] = ("nop" if "jmp" else "jmp")
            result = run_program(tmp)
            if result:
                print(f"Swapped line {i+1}: {k} {v}")
                part2 = result
                break
    
    return part1, part2

if __name__ == "__main__":
    part1, part2 = get_day8()
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")