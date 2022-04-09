p = []

for i in range(3):
    p.append(list(map(int, input().split())))

p = sorted(p, key=lambda x: (x[0], -x[1]))

print()

