I = int(input())
inf = []
arts = []
rec = []

for _ in range(I):
    id, art = map(int, input().split())
    if id in inf:
        index = inf.index(id)
        if art in arts[index]:
            index2 = arts[index].index(art)
            rec[index][index2] += 1
        else:
            arts[index].append(art)
            rec[index].append(1)
    else:
        inf.append(id)
        arts.append([art])
        rec.append([1])

geral = []
for i in range(len(inf)):
    crimes = []
    for j in range(len(arts[i])):
        crimes.append([arts[i][j], rec[i][j]])
    crimes = sorted(crimes, key=lambda x: (-x[1], x[0]))
    geral.append(crimes)

M = 0
frase = input().split()
for item in frase:
    if item.isdigit(): 
        M = int(item)
        break

desc = input()

for _ in range(M):
    rg = int(input())
    if rg in inf:
        index = inf.index(rg)
        print(f"Teje preso, {rg}!")
        for i in range(len(geral[index])):
            print(f"- Art. {geral[index][i][0]}: {geral[index][i][1]} ocorrencia(s).")
    else:
        print(f"Grato, cidadao {rg}.")
    



