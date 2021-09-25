n, m = map(int, input().split())
caminho = list(map(int, input().split()))

atual, tempo = 1, 0

for ponto in caminho:
    if ponto > atual:
        tempo += ponto-atual
    elif ponto < atual:
        tempo += n - atual + ponto
    atual = ponto

print(tempo)