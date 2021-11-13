n = int(input())
grafo = [[] for _ in range(n+1)]
vis = [0 for _ in range(n+1)]

cons = list(map(int, input().split()))

for i in range(n):
    grafo[i+1].append(cons[i])

max = 1
for i in range(n):
    if not vis[i]:
        vis[i] = 1
        caminhos = []
        


print(grafo)