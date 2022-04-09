from pyexpat.errors import XML_ERROR_ABORTED


t = int(input())

for _ in range(t):
    n = int(input())
    pontos = []
    simetrico = True

    for _ in range(n):
        pontos.append(list(map(int, input().split())))
    pontos = sorted(pontos, key=lambda x:[x[0],x[1]])

    if n == 1:
        print("Yes")
        continue
    
    xm2 = pontos[0][0] + pontos[-1][0]
    if n%2 == 1:    # Se for ímpar, confere membro do meio
        if pontos[n//2][0] != xm2:
            print("False")
            break
        else:
            pontos.pop(n//2)

    i = 0
    j = n//2
    simetrico = True
    
    # Todos os pontos esão no meio
    if pontos[0][0] == xm2 and pontos[-1][0] == xm2:
        print("Yes")
        continue

    while(i < n//2):
        if pontos[i][0] == xm2:
            if pontos[-1][0]
    
    if simetrico:
        print("Yes")
    else:
        print("No")
