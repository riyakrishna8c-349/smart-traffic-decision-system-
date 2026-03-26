# display.py

def show(roads):
    print("\nCurrent traffic:")
    for r in roads:
        print(r["road"], "has", r["cars"], "cars")


def show_signal(selected, time):
    print("Green signal for road", selected["road"])
    print("Time:", time, "seconds")
