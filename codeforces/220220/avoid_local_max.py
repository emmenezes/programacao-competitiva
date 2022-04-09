t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = []
    c = 0

    for i in range(1,n-1):
        if a[i] > a[i-1] and a[i] > a[i+1]:
            b.append(i)
    
    if b == []:
        print(0)
        print(*a)
        continue

    # print(f"b: {b}")
    size_b = len(b)
    i = 0
    while i < size_b-1:
        c += 1
        if b[i+1] - b[i] == 2:
            a[b[i]+1] = max(a[b[i]], a[b[i+1]])
            i += 2
        else:
            a[b[i]] = max(a[b[i]]-1, a[b[i]]+1)
            i += 1
    
    if a[b[-1]] > a[b[-1]-1] and a[b[-1]] > a[b[-1]+1]:
        a[b[-1]] = max(a[b[-1]-1], a[b[-1]+1])
        c += 1
        
    print(c)
    print(*a)

