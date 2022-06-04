from collections import deque
graph ={}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def personIsSeller(name):
    return name[-1] == 'm'

searchQueue = deque()
searchQueue += graph["you"]
searched = []
while searchQueue:
    person = searchQueue.popleft()
    if person not in searched:
        if personIsSeller(person):
            print(person, "is a mango seller")
            break
        else:
            searchQueue += graph[person]
            searched.append(person)