c = []
c.append(list(map(int, input().split())))
c.append(list(map(int, input().split())))
c.append(list(map(int, input().split())))

v = []
v.append([c[0][0], c[1][1]])
v.append([c[0][0], c[2][1]])
v.append([c[1][0], c[0][1]])
v.append([c[1][0], c[2][1]])
v.append([c[2][0], c[0][1]])
v.append([c[2][0], c[1][1]])

for vx in v:
    if vx not in c:
        print(*vx)
        break