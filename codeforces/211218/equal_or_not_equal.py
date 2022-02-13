t = int(input())

for _ in range(t):
    s = input()
    tam = len(s)

    op = []
    op.append(s[0])
    for i in range(1,tam-1):
        pass

    if s[tam-1] not in op:
        print("NO")
    else:
        print("YES")
