n = int(input())
ans = 0

for i in range(n):
    coord = list(map(int, input().split()))
    ans += (abs(coord[2] - coord[0]) + 1)*(abs(coord[3] - coord[1]) + 1)

print(ans)
