from math import pi

n = int(input())
r = list(map(int, input().split()))

r.sort(reverse=True)

ans = 0

sig = 0
for rx in r:
    if sig:
        ans -= rx*rx
    else:
        ans += rx*rx
    sig = 1 - sig

print(ans*pi)