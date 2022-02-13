from math import ceil

h1, h2 = map(int, input().split())
a, b = map(int, input().split())

d = h2 - h1

if a*8 >= d:
    # print("a")
    print(0)
elif a - b <= 0:
    # print("b")
    print(-1)
else:
    # print("c")
    days = 0
    d -= a*8    # tempo do primeiro dia
    # d -= a*12   # tempo que percorre no último dia
    # print(f"dist {d}")
    d_day = 12 * (a-b)
    days = ceil(d/d_day)
    print(days)