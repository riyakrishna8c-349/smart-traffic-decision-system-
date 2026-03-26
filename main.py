# main.py

from data import get_roads
from logic import calc_time, find_busy, update
from display import show, show_signal

def run():
    roads = get_roads()
    cycles = 5

    for counter in range(cycles):
        print("\nCycle", counter + 1)

        show(roads)

        selected = find_busy(roads)
        t = calc_time(selected["cars"])

        show_signal(selected, t)

        update(roads, selected)

    print("\nSimulation finished")


# entry point
if __name__ == "__main__":
    run()
