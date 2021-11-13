def dfs(u, vis):
    if vis[u]:
        return 0
    vis[u] = 1
    count = 1
    for v in rel[u]:
        count += dfs(v, vis)
    return count
        

n, m = map(int, input().split())

rel = [[] for _ in range(n+1)]
vis = [0 for _ in range(n+1)]

c = int(input())

if c == 0:
    if m == 1:
        print(f"{n} 1")
    else:
        print(0)
    quit()

for _ in range(c):
    a, b = map(int, input().split())
    rel[a].append(b)
    rel[b].append(a)

quad = []

for u in range(1, n+1):
    if not vis[u]:
        tam = dfs(u, vis) or 0
        quad.append(tam)

max = 0
quant = 0

for q in quad:
    if q >= m:
        quant += 1
        if q > max:
            max = q

if quant == 0:
    print(0)
else:
    print(f"{quant} {max}")

