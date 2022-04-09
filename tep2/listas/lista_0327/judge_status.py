v = {"AC": 0, "WA": 0, "TLE": 0, "RE": 0}

n = int(input())

for _ in range(n):
    vx = input()
    v[vx] += 1

for vx in v:
    print(f'{vx} x {v[vx]}')