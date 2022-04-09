Q = int(input())
A = []

for _ in range(Q):
    cmd = list(map(int, input().split()))
    if cmd[0] == 1:
        A.append(cmd[1])
    elif cmd[0] == 2:
        A.sort()
        Aux = [i for i in A if i <= cmd[1]]
        id = len(Aux) - cmd[2]
        if id >= 0:
            # print(Aux)
            print(Aux[id])
        else:
            print(-1)
    else:
        A.sort()
        Aux = [i for i in A[::-1] if i >= cmd[1]]
        id = len(Aux) - cmd[2]
        if id >= 0:
            # print(Aux)
            print(Aux[id])
        else:
            print(-1)