import numpy as np
import pandas as pd


def rps(them, us):
    score = 0
    match them:
        case "A":
            match us:
                case "X":
                    score += 3
                case "Y":
                    score += 6
        case "B":
            match us:
                case "Y":
                    score += 3
                case "Z":
                    score += 6
        case "C":
            match us:
                case "X":
                    score += 6
                case "Z":
                    score += 3
    match us:
        case "X":
            score += 1
        case "Y":
            score += 2
        case "Z":
            score += 3

    return score


def rps_modifier(them, result):
    us = ""
    match result:
        case "X":
            match them:
                case "A":
                    us = "Z"
                case "B":
                    us = "X"
                case "C":
                    us = "Y"
        case "Y":
            match them:
                case "A":
                    us = "X"
                case "B":
                    us = "Y"
                case "C":
                    us = "Z"
        case "Z":
            match them:
                case "A":
                    us = "Y"
                case "B":
                    us = "Z"
                case "C":
                    us = "X"

    return them, us


def get_day2(infile="./aoc2022/day2_input.txt", part2=False):
    data = np.loadtxt(infile, delimiter=" ", dtype=str)

    df = pd.DataFrame(data)

    if not part2:
        return df.apply(lambda x: rps(x[0], x[1]), axis=1).sum()

    # Modify our actions based on redefined 2nd column
    df = df.apply(lambda x: rps_modifier(x[0], x[1]), axis=1, result_type="expand")

    return df.apply(lambda x: rps(x[0], x[1]), axis=1).sum()


if __name__ == "__main__":
    print("Day 2")
    print(
        f"What would your total score be if everything goes "
        + f"exactly according to your strategy guide?\n[ {get_day2()} ]"
    )
    print(
        f"Following the Elf's instructions for the second column, "
        + "what would your total score be if everything goes exactly "
        + f"according to your strategy guide?\n[ {get_day2(part2=True)} ]"
    )
