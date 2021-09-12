n = int(input())

tam = []
poesia_sucinta = []

for i in range(n):
    linha = input().split()
    tam.append(len(linha))
    for palavra in linha:
        achou = False
        pos = 1
        for termo in poesia_sucinta:
            if palavra == termo:
                achou = True
                poesia_sucinta.append(str(pos))
                break
            pos += 1
        if not achou:
            poesia_sucinta.append(palavra)

i = 0
for num in tam:
    linha = ' '.join(poesia_sucinta[i:i+num])
    i += num
    print(linha)

