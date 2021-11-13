'''
Se houver menos de 3 pessoas, todas elas sairão ao mesmo tempo:
1 - não tem amizades e sai primeiro
2 - cada uma não tem amizades ou tem só uma, e saem juntas primeiro

Se houver 3 ou mais, a ideia é que todas as pessoas conheçam a todas, menos 2 pessoas que não são amigas.
Isso é preciso para que haja primeira saída, pois elas terão n-2 amigos, enquanto todas as outras terão n-1.
Após a saída dessas 2, todas as pessoas terão a mesma quantidade de amizades, n-3.
E esse é o resultado.
'''


t = int(input())
for _ in range(t):
    n = int(input())
    if n < 3:
        print(0)
    else:
        print(n-2)