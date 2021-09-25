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

    m = n
    fator_n = [2]
    atual = 0
    while m != 1:
        while (m%fator_n[atual] == 0):
            m = m/fator_n[atual]
        if (m == 1):
            break
        novo_fator = fator_n[atual]+1
        while (m%novo_fator != 0):
            novo_fator += 1
        fator_n.append(novo_fator)
        atual += 1

    m = n - 1
    fator_n2 = [2]
    atual = 0
    while m != 1:
        while (m%fator_n2[atual] == 0):
            m = m/fator_n2[atual]
        if (m == 1):
            break
        novo_fator = fator_n2[atual]+1
        while (m%novo_fator != 0):
            novo_fator += 1
        fator_n2.append(novo_fator)
        atual += 1
    
    fator = fator_n + fator_n2
    
    primo = n - 3
    encontrado = False

    while not encontrado:
        encontrado = True
        for i in fator:
            if (primo%i == 0):
                primo -= 2
                encontrado = False
                break

    print(n, (n-1), primo)
    print(n*(n-1)*primo)