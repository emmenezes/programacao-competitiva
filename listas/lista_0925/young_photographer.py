n, m = map(int, input().split())

l = r = 0
for _ in range (n):
    a, b = map(int, input().split())
    a, b = min([a,b]), max([a,b])
    if n < a:
        dif = a - n
        if dif > r: r = dif
    elif b > n:
        pass