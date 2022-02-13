n, k = map(int, input().split())
a = list(map(int, input().split()))

b = [[0,0,0] for _ in range(k)]

for i in range(n//k):
    for j in range(k):
        v = a[i*k+j]
        b[j][v] += 1

s = 0
for i in b:
    s += min(i[1], i[2])

print(s)