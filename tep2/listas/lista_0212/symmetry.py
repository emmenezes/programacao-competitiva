# Problema: e se todos os pontos estiverem sobre uma reta no meio

t = int(input())

for _ in range(t):
    n = int(input())
    pontos = []
    simetrico = True

    for _ in range(n):
        pontos.append(list(map(int, input().split())))
    pontos = sorted(pontos, key=lambda x:[x[0],x[1]])
    # print(pontos)
    if n == 1:
        print("Yes")
        continue
    if n%2 == 1:
        pontos_medio = pontos.pop(n//2)[0]
    else:
        ponto_medio = (pontos[0][0]+pontos[-1][0])/2
        if ponto_medio != pontos[0][1] and pontos[0][1] != pontos[-1][1]:
            print("No")
            continue
    for i in range(n//2):
        if pontos[i][0] == ponto_medio and pontos[-i-1][0] == ponto_medio:
            continue
        novo_ponto_medio = (pontos[i][0]+pontos[-i-1][0])/2
        if novo_ponto_medio != ponto_medio or pontos[i][1] != pontos[-i-1][1]:
            simetrico = False
            break
    if simetrico:
        print("Yes")
    else:
        print("No")
