n, m = map(int, input().split())
amizade = "YES"
lacos = []
for i in range(n):
    lacos.append([])

for i in range(m):
    a, b = map(int, input().split())
    a, b = a - 1, b - 1
    lacos[a].append(b)
    lacos[b].append(a)


for i in range(n):
    if (len(lacos[i]) > 1):
        for j in range(len(lacos[i])-1):
            if (lacos[i][j] not in lacos[lacos[i][j+1]]):
                amizade = "NO"
                break

print(amizade)
