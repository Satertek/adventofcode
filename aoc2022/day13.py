import numpy as np
import pandas as pd


def list_it(l):
    if not isinstance(l, list):
        l = list([l])
    return l


def check_pair(left, right):

    for i in range(len(left)):
        if i > len(right):
            print(f"{i} {left} {right}")
            if left[i - 1] == right[i - 1]:
                return False

        # If either left or right value is a list, recursively check that new pair
        elif isinstance(left[i], list) or isinstance(right[i], list):
            left[i] = list_it(left[i])
            right[i] = list_it(right[i])
            if not check_pair(left[i], right[i]):
                return False

        elif left[i] > right[i]:
            return False

    return True


def get_day13(infile="./aoc2022/day13_input.txt", part2=False):
    with open(infile) as f:
        data = f.read().split("\n\n")

    valid_pairs = []
    for i, pair in enumerate(data):
        print(f"Pair {i+1}")
        left, right = list(eval(x) for x in pair.split("\n"))
        if check_pair(left, right):
            valid_pairs.append(i + 1)

    print(valid_pairs)
    return sum(valid_pairs)


# def test_day13():
#     assert get_day13("./aoc2022/day13_test.txt") == 13
# assert get_day13("./aoc2022/day13_test.txt", part2=True) == 0


if __name__ == "__main__":
    # test_day13()
    print("?" + f"\n[ {get_day13()} ]")
    print("?" + f"\n[ {get_day13(part2=True)} ]")


# def check_pair(left, right):
#     if not isinstance(left, list):
#         left = list([left])
#     if not isinstance(right, list):
#         right = list([right])

#     for i in range(len(left)):
#         try:
#             if isinstance(left[i], list) or isinstance(right[i], list):
#                 if not check_pair(left[i], right[i]):
#                     return False
#             elif left[i] > right[i]:
#                 # Right side is smaller, so inputs are not in the right order
#                 return False
#         except IndexError:
#             if len(left) > len(right):
#                 if len(left) > i-1 and len(right) > i-1 and (not isinstance(left[i-1],list)) and (not isinstance(right[i-1],list)):
#                     if left[i-1] >= right[i-1]:
#                         # Right side ran out of items, so inputs are not in the right order
#                         return False
#             if len(left) == 1:
#                 return False

#     return True
