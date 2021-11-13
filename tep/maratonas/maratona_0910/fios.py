f = lambda: map(int, input().split())
n, m = f()
p = [list(range(n + 1)) for x in range(m + 1)]
def g(c, x):
    if x != p[c][x]: p[c][x] = g(c, p[c][x])
    return p[c][x]
for i in range(m):
    a, b, c = f()
    p[c][g(c, a)] = g(c, b)
for j in range(int(input())):
    a, b = f()
    print(sum(g(i, a) == g(i, b) for i in range(m + 1)))