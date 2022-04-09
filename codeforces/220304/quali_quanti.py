t = int(input())

for _ in range(t):
    n = int(input())
    d = list(map(int, input().split()))

    d.sort()
    soma_azul = d[0]
    soma_vermelho = 0
    possivel = False

    i = 1
    while (i < n-i):
        soma_azul += d[i]
        soma_vermelho += d[-i]
        if soma_vermelho > soma_azul:
            possivel = True
            break
        i += 1
    
    if possivel:
        print("YES")
    else:
        print("NO")
