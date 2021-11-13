def dfs(i, u, vis):
    if vis[u]:
        return
    vis[u] = i
    for v in rel[u]:
        dfs(i, v, vis)


n, q = map(int, input().split())

rel = [[] for _ in range(n+1)]
vis = [0 for _ in range(n+1)]

for _ in range(q):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

cand = [0]
i = 1
for u in range(1, n+1):
    if not vis[u]:
        dfs(i, u, vis)
        i += 1

cand = [1 for _ in range(i)]
cand[0] = 0

m = int(input())

if m != 0:
    vot = list(map(int, input().split()))

    for u in range(m):
        cand[vis[vot[u]]] = 0

print(sum(cand))