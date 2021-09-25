posicao = input()

time = posicao[0]
seq = 0

for jogador in posicao:
    if (jogador == time):
        seq += 1
        if (seq == 7):
            print("YES")
            quit()
    else:
        seq = 1
        time = jogador

print("NO")