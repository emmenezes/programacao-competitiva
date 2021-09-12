def resolve(n):
    if (n <= 2):
        print(n)
    elif (n%2 == 1):
        print(n*(n-1)*(n-2))
    elif (n%3 != 0):
        print(n*(n-1)*(n-3))
    else:

        if (n == 6):
            return(60)

        m = n
        fator = [2]
        atual = 0
        while m != 1:
            while (m%fator[atual] == 0):
                m = m/fator[atual]
            if (m == 1):
                break
            novo_fator = fator[atual]+1
            while (m%novo_fator != 0):
                novo_fator += 1
            fator.append(novo_fator)
            atual += 1
        
        
        primo = n - 3
        encontrado = False

        while not encontrado:
            encontrado = True
            for i in fator:
                if (primo%i == 0):
                    primo -= 2
                    encontrado = False
                    break

        return([n, (n-1), primo])


# n = int(input())
# res = resolve(n)
# print(res[0],res[1],res[2])
# print(res[0]*res[1]*res[2])