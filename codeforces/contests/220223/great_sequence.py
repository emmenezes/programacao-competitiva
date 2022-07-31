t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    lena = len(a)
    lenf = 1
    s = 0

    while lena != lenf and lenf != 0:
        m = []
        p = []
        
        lena = len(a)
        for ax in a:
            if ax%x :
                p.append(ax)
            else:
                m.append(ax//x)

        s += len(p)
        # print("m", *m)
        # print("p", *p)
        for id, mx in enumerate(p):
            if mx in m:
                s -= 1
                m.remove(mx)
        # print("s", s)
        a = [i for i in m]
        lenf = len(a)

        # print("a", *a, "\n")

    s += len(a)
    print(s)


