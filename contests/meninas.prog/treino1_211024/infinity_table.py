import math

t = int(input())

for _ in range(t):
    n = int(input())

    r = math.ceil(math.sqrt(n))
    r2 = r**2
    q = (r-1)**2 + 1

    mid = (q + r2)//2

    if n <= mid:
        print(f"{n-q + 1} {r}")
    else:
        print(f"{r} {r2-n+1}")