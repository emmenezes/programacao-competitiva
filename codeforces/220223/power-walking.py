from traceback import print_tb


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()

    rep = []
    f = a[0]
    c = 1
    for ax in a[1:]:
        if ax == f:
            c += 1
        else:
            rep.append(c)
            f = ax
            c = 1
    
    rep.append(c)
    rep.sort()

    lrep = len(rep)
    ans = [lrep for i in range(lrep)]

    for i in range(len(ans), n+1):
        lrep += 1
        ans.append(lrep)

    print(*ans[:-1])
