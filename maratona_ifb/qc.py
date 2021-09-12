import math

n = int(input())

ans = 0

for i in range(n):
    x, y = map(float, input().split())
    d = x**2 + y**2
    if d <= 1:
        ans += 10
    elif d <= 4:
        ans += 9
    elif d <= 9:
        ans += 8
    elif d <= 16:
        ans += 7
    elif d <= 25:
        ans += 6
    elif d <= 36:
        ans += 5
    

print(ans)