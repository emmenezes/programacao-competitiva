n, d = map(int, input().split())
d = 2*d + 1

if n%d == 0:
    print(n//d)
else:
    print(n//d + 1)