n = int(input())

pos, dis = [], []
for _ in range(n):
    posx, disx = map(int, input().split())
    pos.append(posx)
    dis.append(disx)


for i in range(n):
    posi, disi = pos[i], dis[i]
    alvo = posi + disi
    if alvo in pos:
        index = pos.index(alvo)
        contra = pos[index] + dis[index]
        if contra == posi:
            print("YES")
            quit()

print("NO")