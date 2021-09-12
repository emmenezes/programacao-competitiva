def parentesco(nome):
    familia = []
    if nome[1][-5:] == "evich":
        familia.append(nome[1][:-5])
    elif nome[1][-5:] == "ovich":
        familia.append(nome[1][:-5])
    elif nome[1][-5:] == "ichna":
        familia.append(nome[1][:-5])
    elif nome[1][-4:] == "evna":
        familia.append(nome[1][:-4])
    elif nome[1][-4:] == "ovna":
        familia.append(nome[1][:-4])
    else:
        familia.append(nome[1][:-3])

    if nome[2][-3:] == "ina":
        familia.append(nome[2][:-3])
    elif nome[2][-3:] == "ova":
        familia.append(nome[2][:-3])
    elif nome[2][-3:] == "eva":
        familia.append(nome[2][:-3])
    else:
        familia.append(nome[2][:-2])    

    return familia


nome = input().split()
familia = parentesco(nome)

irmao, parente = 0, 0

n = int(input())

for i in range(n):
    pessoa = input().split()
    familia_pessoa = parentesco(pessoa)
    if (familia[0] == familia_pessoa[0] and familia[1] == familia_pessoa[1]):
        irmao += 1
    if (familia[1] == familia_pessoa[1]):
        parente += 1

print(parente, irmao)
