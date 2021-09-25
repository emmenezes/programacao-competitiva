n, a = map(int, input().split())

arvores = list(map(int, input().split()))

caso = -1
melhor_caso = 10000

for i in range(n):
    b = arvores[i] - i*a
    if b > 0:
        alteracoes = 0
        for j in range(n):
            y = b + j*a
            if y != arvores[j]:
                alteracoes += 1
        # print(arvores[i], alteracoes)
        if alteracoes < melhor_caso:
            caso = i
            melhor_caso = alteracoes

if melhor_caso == 0:
    print(0)
    quit()

print(melhor_caso)
y = arvores[caso] - caso*a
for i in range(n):
    tam = arvores[i]
    if tam > y:
        print(f"- {i+1} {tam - y}")
    elif tam < y:
        print(f"+ {i+1} {y - tam}")
    y += a
        