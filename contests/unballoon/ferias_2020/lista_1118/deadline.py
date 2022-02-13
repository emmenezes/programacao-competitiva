from math import ceil, floor, sqrt

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    if d <= n:
        print("YES")
    else:
        x_ceil = sqrt(d) -1
        x_floor = floor(x_ceil)
        x_ceil = ceil(x_ceil)
        opt_ceil = x_ceil + ceil(d/(x_ceil+1))
        opt_floor = x_floor + ceil(d/(x_floor+1))
        # print(x_ceil, opt_ceil)
        # print(x_floor, opt_floor)
        if opt_ceil <= n or opt_floor <= n:
            print("YES")
        else:
            print("NO")
