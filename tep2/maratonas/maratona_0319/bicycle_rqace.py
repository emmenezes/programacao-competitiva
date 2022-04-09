n = int(input())

s = 0
data = []

for _ in range(n+1):
    data.append(list(map(int, input().split())))

for i in range(0, n):
    atual = data[i]
    prox = data[i+1]

    curva = [prox[0] - atual[0], prox[1] - atual[1]]
    print(curva)