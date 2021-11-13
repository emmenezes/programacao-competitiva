n, l = map(int, input().split())

if (n%2 == 1 and l%2 == 1) or l > n -1 :
    print("Nao")
else:
    print("Sim")