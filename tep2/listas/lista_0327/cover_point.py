m = 0

n = int(input())

for _ in range(n):
    xi, yi = map(int, input().split())
    mi = xi + yi
    if mi > m:
        m = mi

print(m)
