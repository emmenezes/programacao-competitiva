n, m = map(int, input().split())

l, r = 0, 1000
for _ in range (n):
    a, b = map(int, input().split())
    a, b = min([a,b]), max([a,b])
    if a > l:   l = a
    if b < r:   r = b
    
    #print(l, r)

if l > r:                   print(-1)
else:
    if l <= m and m <= r:   print(0)
    elif l > m:             print(l-m)
    else:                   print(m-r)