n, m = map(int, input().split())

grafo = [list() for _ in range (n+1)]

for i in range(m):
    a, b = map(int, input().split())
    grafo[a].append(b)
    grafo[b].append(a)

s0 = 0
s1 = 0
s2 = 0
sn = 0
sx = 0
for ponto in grafo:
    if len(ponto) == 0:         s0 += 1
    elif len(ponto) == 1:       s1 += 1
    elif len(ponto) == 2:       s2 += 1
    elif len(ponto) == n -1:    sn += 1
    else:                       sx += 1

if sn == 1 and s1 == n - 1:
    print("star topology")
    quit()

if s0 > 1 or s2 < n - 2 or sx:
    print("unknown topology")
    quit()

# ring and bus topology
visitados = [0 for _ in range(n+1)]
ponto = 1
visitados[1] = 1
while True:
    prox = grafo[ponto][0]
    i = 1
    while visitados[prox] and i < len(grafo[ponto]):
        prox = grafo[ponto][i]
        i += 1
    #print(ponto, prox)
    if i > len(grafo[ponto]) or visitados[prox]:    
        if prox == 1:
            visitados[1] += 1
        break
    ponto = prox
    visitados[prox] = 1

if visitados[1] == 2:
    ring = True
    for item in visitados[2:]:
        if not item:
            ring = False
            break
    if ring:
        print("ring topology")
        quit()

if len(grafo[1]) == 2:
    ponto = 1
    grafo[1].pop(0)
    while True:
        prox = grafo[ponto][0]
        i = 1
        while visitados[prox] and i < len(grafo[ponto]):
            prox = grafo[ponto][i]
            i += 1
        #print(ponto, prox)
        if i > len(grafo[ponto]) or visitados[prox]:    
            if prox == 1:
                visitados[1] += 1
            break
        ponto = prox
        visitados[prox] = 1

bus = True
for item in visitados[2:]:
    if not item:
        bus = False
        break
if bus:
    print("bus topology")
    quit()

#print(visitados)
print("unkown topology")

# print(*grafo, sep='\n')