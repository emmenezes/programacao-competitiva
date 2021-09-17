t = int(input())

for _ in range(t):
    n = int(input())
    mortal = list(map(int, input().split()))
    mortal = list(reversed(mortal))

    cont = 0
    controle = -1
    rodada = 2
    poder = 0
    while (len(mortal)):
        inimigo = mortal.pop()
        if rodada == 0:
            controle = -controle
            rodada = 2
        if controle == 1: # eu
            if not inimigo and rodada == 1:
                rodada = 1
                controle = -1
                #print(inimigo, " - eu matei 1 e deixei o fraco para amigo")
            else:
                rodada -= 1
                #print(inimigo, " - eu precisei matar 1")
        else:       # amigo
            if inimigo and rodada == 1:
                rodada = 1
                controle = 1
                #print(inimigo, " - amigo meu passou")
            elif inimigo:
                poder += 1
                rodada -= 1
                #print(inimigo, " - amigo precisou usar PODER")
            else:
                rodada -= 1
                #print(inimigo, " - era facil e amigo matou")

    print(poder)