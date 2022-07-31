t = int(input())

for _ in range(t):
    n = int(input())
    pos = [0 for _ in range(n+1)]
    f = [0 for _ in range(n+1)]
    o = list(map(int, input().split()))
    for id, value in enumerate(o):
        pos[value] = id + 1
    for i in range(n,0,-1):
        p = (i - pos[n] - sum(f[i:]))
        while p < 0:
            p += n
        f[i] = p
    print(f)