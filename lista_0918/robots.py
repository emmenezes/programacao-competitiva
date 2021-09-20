'''
Referência:
https://codeforces.com/problemset/problem/8/B
'''

pos = [[0,0]]
atual = [0,0]

passos = input()

map = True
for i in range(len(passos)):
    if passos[i] == "L":
        atual[0] -= 1
    elif passos[i] == "R":
        atual[0] += 1
    elif passos[i] == "U":
        atual[1] += 1
    else:
        atual[1] -= 1
    if atual in pos:
        map = False
        break
    else:
        pos.append(atual.copy())

if map:
    #print("OK")
    n = len(pos)
    #print(pos)
    if n > 3:
        for i in range(n-3):
            for j in range(i+3, n):
                #print(i, j)
                if (pos[i][0] == pos[j][0] and abs(pos[i][1] - pos[j][1]) == 1) or pos[i][1] == pos[j][1] and abs(pos[i][0] - pos[j][0]) == 1:
                    print("BUG")
                    quit()
    print("OK")              
else:
    print("BUG")