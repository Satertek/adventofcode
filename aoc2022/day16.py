import re
import numpy as np
import pandas as pd
import numba
from collections import namedtuple
import time
from tqdm import tqdm
from multiprocessing import Pool
import os


def load_data(infile):
    with open(infile) as f:
        data = f.read()
    regex_str = (
        r"Valve (?P<valve>\S+).*=(?P<rate>\d+).*valves? (?P<valve_list>.*)(?:\n|$)"
    )
    regex = re.compile(regex_str)
    data = np.array(regex.findall(data))
    return data


def cave_run(data):
    timer = 1
    pressure = 0
    pressure_per_minute = 0
    opened_valves = []
    message_log = ""
    valve = 'AA'
    while True:
        # Stop if we're out of time
        if timer > 30:
            break

        message_log += f"== Minute {timer} ==\n"

        if opened_valves:
            message_log += f"Valves {', '.join(opened_valves)} are releasing {pressure_per_minute} pressure.\n"
        else:
            message_log += "No valves are open.\n"

        pressure += pressure_per_minute
        message_log += f"Total Pressure: {pressure}\n"

        i = np.where(data == valve)[0]
        _, rate, tunnels = data[i][0]
        rate = int(rate)
        #pressure -= rate  # delay first release of this valve by 1 minute
        tunnels = tunnels.split(",")

        # Open valve in this room and mark it as opened
        if valve not in opened_valves and rate > 0 and np.random.randint(0, 100) > 50:
            pressure_per_minute += rate
            opened_valves.append(valve)
            message_log += f"You open valve {valve} (adding {rate}/min)\n"
            timer += 1
            continue

        # Pick a random room to go to next
        valve = tunnels[np.random.randint(0, len(tunnels))].strip()
        timer += 1

        message_log += f"You move to valve {valve}\n"

    return pressure, message_log

def best_run(df):
    brun = df.iloc[:,0].astype(int).idxmax()
    return [df.iloc[brun, :].to_numpy()]

def cave_runs(data, count=10):
    runs = list(cave_run(data) for _ in tqdm(range(count)))
    df = pd.DataFrame(runs)
    return best_run(df)
    

def get_day16(infile="./aoc2022/day16_input.txt", part2=False):

    data = load_data(infile)

    # More Firepower
    all_results = []
    results = []
    with Pool(os.cpu_count()) as p:
        for _ in range(640):
            results.append(p.apply_async(cave_runs, (data,int(100000))))
        for each in results:
            all_results.append(each.get())
        all_results = np.vstack(all_results)
        df = pd.DataFrame(all_results)

    brun = best_run(df)[0]
    print(brun[1])
    return brun[0]

if __name__ == "__main__":
    print("?" + f"\n[ {get_day16()} ]")
    # print("?" + f"\n[ {get_day16(part2=True)} ]")
