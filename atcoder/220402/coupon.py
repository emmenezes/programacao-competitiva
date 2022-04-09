s = []

n, k, x = map(int, input().split())
a = list(map(int, input().split()))

p = 0
for i in range(n):
    if k and a[i] > x:
        r = a[i]//x
        if r > k:
            r = k
        k -= r
        p += a[i] - r*x
        s.append(a[i] - r*x)
    else:
        s.append(a[i])
        p += a[i]

if k:
    s.sort()
    s.reverse()
    m = len(s)
    for i in range(k):
        if i == m:
            break
        p -= s[i]

print(p)