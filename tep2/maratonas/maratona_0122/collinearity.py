def check(reta):
    reta = sorted(reta)
    for i in range(len(reta)-2):
        if reta[i] == reta[i+1] and reta[i] == reta[i+2]:
            return True
    return False

retas = []
pontos = []
vertical = []
horizontal = []
colinear = False

n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    if not colinear:
        for reta in retas:
            yt = reta[0]*x + reta[1]
            if yt == y:
                colinear = True
                continue
        for ponto in pontos:
            numerador = ponto[1] - y
            denominador = ponto[0] - x
            if not numerador:
                horizontal.append(y)
                continue
            if not denominador:
                vertical.append(x)
                continue
            a = numerador/denominador
            b = y - x*a
            retas.append([a,b])
        pontos.append([x,y])
    # print(retas)
    # print(pontos)

if colinear:
    print("Yes")
else:
    if not check(horizontal):
        if not check(vertical):
            print("No")
            quit()
    print("Yes")
   