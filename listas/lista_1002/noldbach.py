n, k = map(int, input().split())

# Encontra primos do intervalo

primos = []

i = 3
for i in range(3, n+1, 2):
    e_primo = True
    for primo in primos:
        if i%primo == 0:
            e_primo = False
            break
    
    if e_primo:
        primos.append(i)

#print(primos)

cont = 0
for index, primo in enumerate(primos[:-1]):
    segundo_primo = primos[index+1]
    possivel_primo = primo + segundo_primo + 1
    #print(possivel_primo)
    if possivel_primo in primos:    
        cont += 1
    if cont == k:
        print("YES")
        quit()
if cont == k:
    print("YES")
else:
    print("NO")