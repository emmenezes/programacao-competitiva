def resolve(k):
    vis[k] = 1
    for i in grafo[k]:
        if vis[i] == 0:    resolve(i)


n, e = map(int, input().split())

vis = [0 for _ in range(n+1)]
grafo = [[] for _ in range(n+1)]
c = 0

for _ in range(e):
    x, y = map(int, input().split())
    grafo[x].append(y)

for i in range(1, n+1):
    resolve(i) 
    c += sum(vis) - 1
    vis = [0 for _ in range(n+1)]

print('%.2f'%(c*100/(n*(n-1))))