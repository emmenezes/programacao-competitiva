n, m = map(int, input().split())

data = list(map(int, input().split()))
ans = 0
res = 0

for i in range(n):
    ans += data[i]//m
    res += data[i]%m

ans += res//m

print(ans*m)