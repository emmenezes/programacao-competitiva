n = int(input())
a = list(map(int, input().split()))
s = [sum(a[0:i+1]) for i in range(n)]

maxv = 0
asum = 0

print(s)

for i in range(n):
    asum += s[i]
    print(asum)
    if asum > maxv:
        maxv = asum

print(maxv)