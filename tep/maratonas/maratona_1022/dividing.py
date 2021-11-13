n = int(input())

if n == 2:
    print(1)
    print("1 1")
    quit()

if n == 3:
    print(0)
    print("2 1 2")
    quit()

k = n*(n+1)/2

if k%2 == 0:
    print(0)
    l = [n//2, n]
    for i in range(n-3, 0, -4):
        l.append(i)
        if i-1 > 0:
            l.append(i-1)
    print(*l)    
else:
    print(1)
    l = []
    if (n-1)%4 == 0:
        l = [n//2 + 1, n]
    else:
        l = [n//2, n]
    for i in range(n-3, 0, -4):
        l.append(i)
        if i-1 > 0:
            l.append(i-1)
    print(*l)


