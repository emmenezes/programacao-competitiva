t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    w = list(map(int, input().split()))
    w.sort()
    total = sum(w)
    if total == x:
        print("NO")
        continue
    s = 0
    for i in range(n-1):
        if sum(w[0:i+1]) == x:
            w[i], w[-1] = w[-1], w[i]
    print("YES")
    print(*w)