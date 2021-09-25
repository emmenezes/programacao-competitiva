m = 1999992
fator = [2]
atual = 0
while m != 1:
    while (m%fator[atual] == 0):
        m = m/fator[atual]
    if (m == 1):
        break
    novo_fator = fator[atual]+1
    while (m%novo_fator != 0):
        novo_fator += 1
    fator.append(novo_fator)
    atual += 1

print(fator)