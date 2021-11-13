data = []
data.append(input())
data.append(input())
data.append(input())

players = ["F", "M", "S"]
r = p = s = 0

for i in data:
    if i == "rock": r += 1
    elif i == "paper": p += 1
    else: s += 1

if p == 1 and r == 2:
    print(players[data.index("paper")])
elif s == 1 and p == 2:
    print(players[data.index("scissors")])
elif r == 1 and s == 2:
    print(players[data.index("rock")])
else:
    print("?")



