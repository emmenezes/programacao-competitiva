n = int(input())

coords = []

for _ in range(n):
    x, _ = map(int, input().split())
    coords.append(x)

possible = True
positive = 0
negative = 0
for cx in coords:
    if cx > 0:
        positive += 1
    else:
        negative += 1
    if positive >= 2 and negative >= 2:
        possible = False
        break

if (possible):
    print("Yes")
else:
    print("No")

