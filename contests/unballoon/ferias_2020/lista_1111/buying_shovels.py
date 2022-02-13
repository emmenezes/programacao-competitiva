from math import sqrt

def maior_divisor(a, b):
    m = 1
    for i in range(2, min(int(sqrt(a)), b)+1):
        if a%i == 0:
            m = i
    return a//m

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k >= n:
        print(1)
    else:
        q = maior_divisor(n, k)
        if q <= k:
            print(min(q, n//q))
        else:
            print(q)
        