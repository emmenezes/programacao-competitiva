n, m = map(int, input().split())

a = []
b = []
c = []
for _ in range(m):
    ax, bx = map(int, input().split())
    a.append(ax)
    b.append(bx)
    c.append(list(map(int, input().split())))