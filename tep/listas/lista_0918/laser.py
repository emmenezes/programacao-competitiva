t = int(input())

for _ in range(t):
    n, m, x1, y1, x2, y2 = map(int, input().split())

    # 1) Descobrir área

    e = min(x1, x2)       # direita
    d = min(n-x1, n-x2)     # esquerda
    b = min(y1,y2)        # baixo
    c = min(m-y1,m-y2)      # cima
    #print(e,c,d,b)

    A = 2*(e+d)*(c+b)

    # 2) Achar a primeira quina de 2 mais próxima de 1
    # Organização das quinas:
    # 2 3
    # 1 4

    As = 0
    if x1 <= x2 and y1 <= y2:
        xq, yq = x2-e+1, y2-b+1
        if x1-e+1 <= xq and xq <= x1+d and y1-b+1 <= yq and yq <= y1+c:
            #print("Quina 1 dentro")
            l = x1+d-xq+1
            a = y1+c-yq+1
            As = l*a
        #else: 
            #print("Quina 1 fora")
    elif x1 <= x2:
        xq, yq = x2-e+1, y2+c
        #print(xq,yq)
        if x1-e+1 <= xq and xq <= x1+d and y1-b+1 <= yq and yq <= y1+c:
            #print("Quina 2 dentro")
            l = x1+d-xq+1
            a = yq-y1+b
            As = l*a
            #print(l, a)
        #else: 
            #print("Quina 2 fora")
    elif x1 > x2 and y1 >= y2:
        xq, yq = x2+d, y2+c
        #print(xq,yq)
        if x1-e+1 <= xq and xq <= x1+d and y1-b+1 <= yq and yq <= y1+c:
            #print("Quina 3 dentro")
            l = xq-x1+e
            a = yq-y1+b
            As = l*a
            #print(l, a)
        #else: 
            #print("Quina 3 fora")
    else:
        xq, yq = x2+d, y2-b+1
        if x1-e+1 <= xq and xq <= x1+d and y1-b+1 <= yq and yq <= y1+c:
            #print("Quina 4 dentro")
            l = xq-x1+e
            a = y1+c-yq+1
            As = l*a
        #else: 
            #print("Quina 4 fora")

    #print(n*m-A+As, n*m, A, As)
    print(n*m-A+As)

