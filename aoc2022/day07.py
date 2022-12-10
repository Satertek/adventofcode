import pandas as pd


def cmd_output(data):
    cmd_out = []
    for line in data:
        if line[0] == "$":
            return cmd_out
        else:
            cmd_out.append(line)
    return cmd_out


def add_file(d, directory, name, size):
    directory = directory.replace("//", "/")
    if d.get(directory) == None:
        d[directory] = {}
    d[directory][name] = size
    return d


def create_dir(d, directory, name):
    if d.get(directory) == None:
        d[directory] = {}
    return d


def get_day07(infile="./aoc2022/day07_input.txt", part2=False):
    with open(infile) as f:
        data = f.read().split("\n")

    # Build our filesystem as a dictionary
    drive = {}
    directory = ""
    for i, line in enumerate(data):
        # Create files and directories when the ls command is seen
        if line == "$ ls":
            cmd_out = cmd_output(data[i + 1 :])
            if cmd_out:
                working_directory = directory
                for cmd in cmd_out:
                    if "dir" in cmd:
                        drive = create_dir(drive, working_directory, cmd.split()[1])
                    else:
                        size, name = cmd.split()
                        drive = add_file(drive, working_directory, name, size)
        # Change the current working path if cd is seen
        elif line == "$ cd ..":
            directory = "/".join(directory.split("/")[:-2]) + "/"
        elif line == "$ cd /":
            directory = "/"
        elif " cd " in line:
            directory += line.split()[2] + "/"

    # Calculate the size of each folder
    drive = pd.DataFrame(drive).fillna(0).astype(int)
    totals = drive.sum()

    # Add the value of all child folders to the parent folder
    for i, parent in enumerate(totals.keys()):
        for j, child in enumerate(totals.keys()):
            if parent in child and parent != child:
                totals[i] += totals[j]

    # If part 2, find directory to delete
    if part2:
        delete_size = 30000000 - (70000000 - totals["/"])
        totals = totals[totals >= delete_size]
        return totals.sort_values().reset_index().to_numpy()[0]

    # If part 1, get totals of directories under 100k
    totals = totals[totals <= 100000]
    if not part2:
        return totals.sum()


def test_day07():
    assert get_day07("./aoc2022/day07_test.txt") == 95437
    assert get_day07("./aoc2022/day07_test.txt", part2=True)[1] == 24933642


if __name__ == "__main__":
    test_day07()
    print(
        "What is the sum of the total sizes of those directories?"
        + f"\n[ {get_day07()} ]"
    )
    print("Which directory should be deleted?" + f"\n[ {get_day07(part2=True)} ]")
