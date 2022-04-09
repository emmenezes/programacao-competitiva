t = int(input())


for k in range(t):
    input()
    n, m = map(int, input().split())
    d = []
    for i in range(m):
        l = list(map(int, input().split()))
        l.append(i+1)
        d.append(l)
    if m != 2*n:
        d = sorted(d, key=lambda x:x[1])
        d = sorted(d[:n*2], key=lambda x:x[0])
    else:
        d = sorted(d, key=lambda x:x[0])

    print(sum(i[1] for i in d))
    for i in range(n):
        print(f'{d[i][2]} {d[-1-i][2]}')
    if k != t - 1:
        print()
