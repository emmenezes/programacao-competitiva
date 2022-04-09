n, h, k = map(int, input().split())
a = list(map(int, input().split()))

i = 0
s = 0
t = 0
while (i < n):
    p = a[i]
    d = h - p
    if s > d:
        r = (s - d)//k
        if (s - d)%k:
            r += 1
        s -= r*k
        if s < 0:
            s = 0
        t += r
    s += p
    i += 1

p = s//k
if s%k:
    p += 1
t += p

print(t)