def start_index(data, markers):
    offset = 0
    for i in range(len(data) - markers):
        if len(set(data[i : i + markers])) == markers:
            return offset + markers
        offset += 1


def get_day06(infile="./aoc2022/day06_input.txt", part2=False):
    with open(infile) as f:
        data = f.read()

    if not part2:
        return start_index(data, 4)
    else:
        return start_index(data, 14)


def test_day06():
    assert get_day06("./aoc2022/day06_test.txt") == 7
    assert get_day06("./aoc2022/day06_test.txt", part2=True) == 19


if __name__ == "__main__":
    test_day06()
    print(
        "With 4 distinct characters, how many characters need to be processed before the"
        + " first start-of-packet marker is detected?"
        + f"\n[ {get_day06()} ]"
    )
    print(
        "With 14 distinct characters, how many characters need to be processed before the"
        + " first start-of-message marker is detected?"
        + f"\n[ {get_day06(part2=True)} ]"
    )
