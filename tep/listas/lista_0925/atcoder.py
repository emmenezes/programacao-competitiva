entrada = input()

atgc = "ATGC"
maior = 0
atual = 0

for letra in entrada:
    if letra in atgc:
        atual += 1
    elif atual > maior:
        maior = atual
        atual = 0

if atual > maior:
    maior = atual

print(maior)