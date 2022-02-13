from json.encoder import INFINITY


t = int(input())

for _ in range(t):
    n = int(input())
    np = list(map(int, input().split()))
    m = int(input())
    mq = list(map(int, input().split()))

    npar = 0
    nimpar = 0
    for npp in np:
        if npp%2 == 0:
            npar += 1
        else:
            nimpar += 1
    
    mpar = 0
    mimpar = 0
    for mqq in mq:
        if mqq%2 == 0:
            mpar += 1
        else:
            mimpar += 1
    
    print(mpar*npar + nimpar*mimpar)


    
