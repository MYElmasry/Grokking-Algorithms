statesNeeded = set(["mt", "wa", "or", "id", "nv", "ut", "ca","az"])
stations = {}
stations["kone"] = ("id", "nv", "ut")
stations["ktwo"] = ("wa", "id", "mt")
stations["kthree"] = ("or", "nv", "ca")
stations["kfour"] = ("nv", "ut")
stations["kfive"] = ("ca", "az")

finalStation = set()
while statesNeeded:
    bestStation = None
    statesCovered = set()
    for station, statesForStation in stations.items():
        covered = statesNeeded.intersection(statesForStation)
        if len(covered) > len(statesCovered):
            bestStation = station
            statesCovered = covered
    statesNeeded -= statesCovered
    finalStation.add(bestStation)
    
print(finalStation)