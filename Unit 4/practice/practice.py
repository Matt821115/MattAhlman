based_teams = ["118 Robonauts", 
               "3276 Toolcats", 
               "4414 HighTide", 
               "4607 C.I.S.", 
               "6800 Valor", 
               "7028 Binary Battalion"]

print("Based teams:")
print("Last: " + based_teams[-1])
print("First: " + based_teams[0])
print("Third: " + based_teams[2])

print()
based_teams.append("6045 Sabre Robotics")
print("Last: " + based_teams[-1])
print("Based teams:\n" + str(based_teams))

print()
based_teams.remove("6045 Sabre Robotics")
print("Last: " + based_teams[-1])
print("Based teams\n" + str(based_teams))

print()
based_teams.insert(4, "6045 Sabre Robotics")
print("Last: " + based_teams[-1])

print("Based teams\n" + str(based_teams))

based_teams.pop(0)

print("\n\n")
for team in based_teams:
    print(team)

print("\n\n\n")
based_teams = [
    118,
    3276,
    4414,
    4607,
    6800,
    7028,
    6045
    ]
print("Based Teams:\n" + str(based_teams))
print("Minimum: " + str(min(based_teams)))
print("Maximum: " + str(max(based_teams)))
print("Team count: " + str(len(based_teams)))

based_teams.sort()
print("Based Teams:\n" + str(based_teams))


print("\n\n")
for team in based_teams:
    print(team)