n = int(input())
c = list(map(int, input().split()))
data = [0]
pos = 1

for i in range(n):
    line = list(map(int, input().split()))
    for j, item in enumerate(line):
        # [numero, pos atual]
        data.append([item, [i+1, j+1]])
    
passos = []
for i in range(1, sum(c)+1):
    atual = data[i]
    while i != atual[0]:
        troca = data[atual[0]]
        atual[1], troca[1] = troca[1], atual[1]
        passos.append([*troca[1], *atual[1]])
        data[atual[0]] = atual
        data[i] = troca
        atual = data[i]
    # print(data)

n = len(passos)
print(n)
for i in range(n):
    print(*passos[i])


