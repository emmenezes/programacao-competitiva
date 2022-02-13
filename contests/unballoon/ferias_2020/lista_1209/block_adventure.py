t = int(input())

for s in range(t):
    n, m, k = map(int, input().split())
    h = list(map(int, input().split()))

    fim = True
    i = 0
    for i in range(0, n-1):
        d = h[i+1]-h[i] 
        # print(f"Mochila: {m}, Distância: {d}, Pos: {i}")
        if d - m <= k:
            m += k - d
        else:
            print("NO")
            fim = False
            break
    if fim and i >= n-2:
        print("YES")
