def dfs(u, visitado):
    if visitado[u]:
        return
    
    visitado[u] = True

    print(u)

    for v in adj[u]:
        dfs(v, visitado)


def pontos_conectados (n):
    visitado = [False for _ in range(n)]

    count = 0

    for u in range(n+1):
        if not visitado[u]:
            print(f"Component {count := count+1} :")
            dfs(u, visitado)
    
    return count
