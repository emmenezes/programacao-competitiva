from math import ceil

n, x, t = map(int, input().split())
p = ceil(n/x)

print(p*t)