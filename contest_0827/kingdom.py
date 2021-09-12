t = int(input())

for i in range (t):
    n = int(input())
    princes = []
    princesses = []
    for j in range (n+1):
        princes.append(j)
    for j in range(n):
        married = False
        princess = list(map(int, input().split()))
        if princess[0] != 0:
            for k in range(1,len(princess)):
                if princes[princess[k]] != 0:
                    princes[princess[k]] = 0
                    married = True
                    break
        if not married:
            princesses.append(j+1)

    if len(princesses) == 0:
        print("OPTIMAL")
    else:
        for j in range(n+1):
            prince = 0
            if (princes[j] != 0):
                prince = princes[j]
                break
        print("IMPROVE")
        print(princesses[0], prince)