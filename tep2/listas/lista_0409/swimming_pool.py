n = int(input())
v = []
a = 0

for i in range(n):
    v.append(list(map(int, input().split())))

if n <= 1:
    print(-1)
else:
    if n == 2:
        if v[0][0] == v[1][0] or v[0][1] == v[1][1]:
            print(-1)
        else:
            a = abs(v[0][0] - v[1][0])*abs(v[0][1] - v[1][1])
            print(a)
    elif n == 3:
        if v[0][0] != v[1][0] and v[0][1] != v[1][1]:
            # Vertices de referência 0 e 1
            a = abs(v[0][0] - v[1][0])*abs(v[0][1] - v[1][1])
            print(a)
        elif v[0][0] != v[2][0] and v[0][1] != v[2][1]:
            # Vertices de referência 0 e 2
            a = abs(v[0][0] - v[2][0])*abs(v[0][1] - v[2][1])
            print(a)
        else:
            # Vertices de referência 1 e 2
            a = abs(v[2][0] - v[1][0])*abs(v[2][1] - v[1][1])
            print(a)
    else:
        if v[0][0] != v[1][0] and v[0][1] != v[1][1]:
            # Vertices de referência 0 e 1
            a = abs(v[0][0] - v[1][0])*abs(v[0][1] - v[1][1])
            print(a)
        elif v[0][0] != v[2][0] and v[0][1] != v[2][1]:
            # Vertices de referência 0 e 2
            a = abs(v[0][0] - v[2][0])*abs(v[0][1] - v[2][1])
            print(a)
        else:
            # Vertices de referência 0 e 3
            a = abs(v[0][0] - v[3][0])*abs(v[0][1] - v[3][1])
            print(a)
