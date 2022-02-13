t = int(input())

for _ in range(t):
    n = int(input())
    m = []
    d = []
    for _ in range(2*n):
        x, y = input().split()
        if x == "0":
            d.append(abs(int(y)))
        else:
            m.append(abs(int(x)))
    s = 0
    d.sort()
    m.sort()
    for i in range(n):
        s += pow(m[i]*m[i] + d[i]*d[i],0.5)
    print(s)