from math import sqrt

r, d = map(int, input().split())

n = int(input())

s = 0
for i in range(n):
    x, y, rs = map(int, input().split())
    dcentro = sqrt(x*x + y*y)
    dmenos = dcentro - rs
    dmais = dcentro + rs
    if dmenos >= d  and dmais <= r:
        s += 1

print(s)