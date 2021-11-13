entrada = input()
pilha = []

for parentese in entrada:
    print(pilha)
    if parentese == "(":
        pilha.append(1)
    else:
        try:
            ultimo = pilha[-1]
        except:
            continue
        print(ultimo)
        if ultimo == 1:
            pilha[-1] = 2
            for el in range(1, len(pilha)):
                if pilha[-el] > 1:
                    val = pilha.pop()
                    pilha[-1] += val
                else:
                    break
        if ultimo > 1:
            try:
                penultimo = pilha[-2]
            except:
                continue

            val = pilha.pop()
            pilha[-1] += val + 1

print(pilha)
            