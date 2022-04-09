t = int(input())

for _ in range(t):
    n = int(input())
    x, y = 0, 0
    mapa = []
    for _ in range(n):
        xi, yi = map(int, input().split())
        mapa.append([xi,yi])
    mapa = set(mapa)
    
    xn = x/n
    yn = y/n
