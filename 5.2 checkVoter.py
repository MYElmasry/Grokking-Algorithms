voted = {}

def checkVoter(name):
    if voted.get(name):
        print("Kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

checkVoter("Tom")

checkVoter("Tom")

checkVoter("mike")

# print(voted.get("mike"))
# print(voted["mike"])