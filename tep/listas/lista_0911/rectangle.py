'''
Referências
* https://codeforces.com/blog/entry/389


Situações:

* Existem mais de 4 coordenadas
* A área é 0
* Checa se os lados estão corretos (tipo se dois lados são iguais)

'''

r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))
r4 = list(map(int, input().split()))

coord = {}
vertical = horizontal = 0
for r in [r1,r2,r3,r4]:
    if r[0] == r[2] and r[1] != r[3]:       # x1 e x2 iguais, mas pontos distintos
        vertical += 1
    elif r[1] == r[3] and r[0] != r[2]:     # y1 e y2 iguais, mas pontos distintos
        horizontal += 1
    if (r[0],r[1]) not in coord:
       coord[(r[0],r[1])] = 1
    else:
       coord[(r[0],r[1])] += 1
    if (r[2],r[3]) not in coord:
       coord[(r[2],r[3])] = 1
    else:
       coord[(r[2],r[3])] += 1

res = False
if vertical == 2 and horizontal == 2:
    res = True
    for valor in coord.values():
        if valor != 2:
            res = False
            break

print("YES") if res else print("NO")
