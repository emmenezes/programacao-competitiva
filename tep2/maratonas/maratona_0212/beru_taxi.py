taxis = []
t = 100000

a, b = map(int, input().split())
n = int(input())

for _ in range(n):
    x, y, v = map(int, input().split())

    d = ((a-x)**2 + (b-y)**2)**0.5
    tx = d/v
    t = min(t, tx)

print(t)



