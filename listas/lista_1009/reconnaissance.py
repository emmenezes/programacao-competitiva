n, d = map(int, input().split())

data = list(map(int, input().split()))
data = sorted(data)

ans = 0
for i in range(n-1):
    j = i + 1
    while j < n and data[j]-data[i] <= d:
        j += 1
        ans += 2

print(ans)