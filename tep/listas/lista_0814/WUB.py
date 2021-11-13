musica = input()
letra = []

while (len(musica)):
    if (musica[0:3] == "WUB"):
        musica = musica[3:]
        continue
    else:
        for i in range(len(musica)):
            if (musica[i:i+3] == "WUB"):
                letra.append(musica[0:i])
                musica = musica[i:]
                break

print(*letra, sep = " ")