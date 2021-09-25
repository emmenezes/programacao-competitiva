t = int(input())

ans = []

for i in range (t):
    n = int(input())
    data =list(map(int, input().split()))

    degenerate = False
    for j in range (n-2):
        for k in range (j+1, n-1):
            for l in range (k+1,n):
                if (data[j]+data[k] <= data[l]):
                    degenerate = True
                    ans.append([j+1, k+1, l+1])
                    break
            if degenerate:
                break
        if degenerate: 
            break
    
    if not degenerate:
        ans.append([-1])

for item in ans:
    print(*item, sep=' ')