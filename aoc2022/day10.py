import numpy as np
import pandas as pd


def get_day10(infile="./aoc2022/day10_input.txt", part2=False):
    cycle = 1

    data = [line.strip().split(" ") for line in open(infile)]
    data = pd.DataFrame(data).to_numpy()  # clean up 2nd column

    # Cycle, diff(X)
    cycle_table = [[1, 1]]

    for cmd in data:
        instruction, value = cmd

        if instruction == "addx":
            cycle_table.append([cycle + 1, 0])
            cycle_table.append([cycle + 2, int(value)])
            cycle += 2
        else:  # NOP
            cycle_table.append([cycle + 1, 0])
            cycle += 1

    cycle_table = pd.DataFrame(cycle_table).groupby(0).sum()
    cycle_table["X"] = cycle_table[1].cumsum()

    if not part2:
        signal = cycle_table[(cycle_table.index + 20) % 40 == 0]
        return (signal.index * signal["X"]).sum()
    else:

        crt = np.arange(0, 240)
        sprite = cycle_table["X"].to_numpy()
        pixels = np.array(["."] * 240)

        for beam in crt:
            s = sprite[beam]
            active_sprites = [s - 1, s, s + 1]
            if beam % 40 in active_sprites:
                pixels[beam] = "#"

        pixels = pixels.reshape(6, 40)
        pixels = list("".join(x) for x in pixels)

        return pixels


def test_day10():
    assert get_day10("./aoc2022/day10_test.txt") == 13140
    assert get_day10("./aoc2022/day10_test.txt", part2=True) == (
        [
            "##..##..##..##..##..##..##..##..##..##..",
            "###...###...###...###...###...###...###.",
            "####....####....####....####....####....",
            "#####.....#####.....#####.....#####.....",
            "######......######......######......####",
            "#######.......#######.......#######.....",
        ]
    )


if __name__ == "__main__":
    test_day10()
    print("What is the sum of these six signal strengths?" + f"\n[ {get_day10()} ]")
    print("What eight capital letters appear on your CRT?")
    print("\n".join(get_day10(part2=True)))
