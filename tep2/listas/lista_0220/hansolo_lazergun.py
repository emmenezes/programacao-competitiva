from math import gcd

n, x0, y0 = map(int, input().split())

retas = []
for _ in range(n):
    x, y = map(int, input().split())
    if x == x0:
        retas.append('x')
        continue
    a = (y-y0)/(x-x0)
    retas.append(a)

retas = set(retas)
print(len(retas))