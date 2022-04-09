k = int(input())

for _ in range(k):
    n, x, t = map(int, input().split())
    if x > t:
        print(0)
    else:
        s = 0
        r = t//x
        if n < r:
            s += ((n)*(n-1)) >> 1
        else:
            s += (n-r)*r
            s += (r*(r-1)) >> 1
        print(s)