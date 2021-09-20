def swaps(a, b):
    count = 0
    s = []
    i = j = 0
    ai, bj = a[i], b[j]
    while ai > bj:
        j += 1
        bj = b[j]
    s.append(j)
    
    i = j = 0
    ai, bj = a[i], b[j]
    while ai > bj:
        i += 1
        ai = a[i]
    s.append(i)
    
    i = j = x = y = 0
    ai, bj = a[i], b[j]
    while ai > bj:
        i += 1
        if ai > a[i]:   ai = a[i]; x = i
        if ai < bj:
            break
        j += 1
        if bj < b[j]:   bj = b[j]; y = j
    s.append(x+y)

    return min(s)

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(swaps(a,b))
