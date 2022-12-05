import numpy as np
from queue import LifoQueue, Empty

def get_day05(infile="./aoc2022/day05_input.txt", part2=False):
    with open(infile) as f:
        crates, procedure = f.read().split("\n\n")
        procedure = procedure.split("\n")

    # Create a 2D array of stacked crates
    crates = crates.split("\n")

    crates = np.loadtxt(
        (
            x.replace(" [", ",").replace("    ", ",").replace("]", "").replace("[", "")
            + ","
            for x in crates[:-1]
        ),
        delimiter=",",
        dtype=str,
    )

    # Reverse order of crates in each column so they are placed in the LIFO in the correct order
    crates = crates[::-1]

    # Put all the crates in LIFO queues
    stacks = []
    for col in range(crates.shape[1]):
        stacks.append(LifoQueue())
        for crate in crates[:, col]:
            if crate.strip():
                stacks[-1].put(crate.strip())

    # Create a 2D array of our procedure with 3 columns:
    #    Quantity, Start, End
    procedure = np.loadtxt(
        (
            x.replace("move", "").replace("from", ",").replace("to", ",")
            for x in procedure
        ),
        delimiter=",",
        dtype=int,
    )

    if not part2:
        for qty, start, end in procedure:
            for _ in range(qty):
                stacks[end - 1].put(stacks[start - 1].get(block=False))
    else:
        for qty, start, end in procedure:
            crate_mover = []
            # Pick them up again one at a time
            for _ in range(qty):
                crate_mover.append(stacks[start - 1].get(block=False))
            # But reverse the order to simulate the actual CrateMover 9001 picking them all up at once
            crate_mover = crate_mover[::-1]
            for i in range(qty):
                stacks[end - 1].put(crate_mover[i])

    # Join together the characters from top of each stack (skip a stack if it's empty)
    message = "".join(x.queue.pop() for x in stacks if len(x.queue) > 0)

    return message

def test_day05():
    assert get_day05("./aoc2022/day05_test.txt") == "CMZ"
    assert get_day05("./aoc2022/day05_test.txt", part2=True) == "MCD"


if __name__ == "__main__":
    test_day05()
    print(
        "After the rearrangement procedure completes, what crate ends up on top of each stack?"
        + f"\n[ {get_day05()} ]"
    )
    print(
        "After the CrateMover 9001 procedure completes, what crate ends up on top of each stack?"
        + f"\n[ {get_day05(part2=True)} ]"
    )
