n = int(input())

c = list(map(int, input().split()))
b = list(map(int, input().split()))

c = sorted(c)
b = sorted(b)

max = 0
for i in range(n):
    dif = abs(c[i] - b[i])
    if dif > max:   max = dif

print(dif)