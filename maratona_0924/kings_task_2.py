n = int(input())
data = list(map(int, input().split()))

passos = [0 for _ in range(n*2)]
impar = -1
impossivel = False
for index, num in enumerate(data):
    num = num-1
    if num%2 == 1:
        if impar == -1:
            impar = index%2
        else:
            if index%2 != impar:
                impossivel = True
    if impossivel: break

    cont = 0
    paridade = num%2
    # print(index, num, paridade)
    while (index != num and cont <= n):
        cont += 1
        if index%2 == paridade:
            if index >= n:
                index -= n
            else:
                index += n
        else:
            if index%2 == 1:
                index -= 1
            else:
                index += 1
    
    print(index, cont)
    if cont > n:
        impossivel = True
        break
    
    
    passos[num] = cont

res = passos[0]
print(passos)
for i in passos[1:]:
    if i != res:
        impossivel = True
        break

if impossivel:
    print(-1)
else:
    print(res)



'''
Algumas observações:
- Só é resolvível se cada número estiver em uma das 4 posições válidas:
    - Posição certa
    - Posição certa adjacente
    - Posição certa + n
    - Posição certa adjacente + n

- Melhor
    - Ou todos os ímpares estão na posição certa, ou tá errado
'''