n = int(input())

if (n <= 2):
    print(n)
elif (n%2 == 1):
    print(n*(n-1)*(n-2))
elif (n%3 != 0):
    print(n*(n-1)*(n-3))
else:
    if (n == 6):
        print(60)
        quit()
    primo = n - 3
    encontrado = False
    while (not encontrado):
        i = 3
        while i*i < primo:
            if (primo%i == 0):
                break
            i += 2
        if (i*i > primo):
            encontrado = True
        else:
            primo -= 2
    print(n, (n-1), primo)
    print(n*(n-1)*primo)