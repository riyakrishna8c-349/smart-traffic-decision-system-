# logic.py

def calc_time(v):
    if v > 20:
        return 55
    elif v > 10:
        return 35
    else:
        return 20


def find_busy(roads):
    busy = roads[0]
    for r in roads:
        if r["cars"] > busy["cars"]:
            busy = r
    return busy


def update(roads, chosen):
    for r in roads:
        if r == chosen:
            r["cars"] -= 10
            if r["cars"] < 0:
                r["cars"] = 0
        else:
            r["cars"] += 3
