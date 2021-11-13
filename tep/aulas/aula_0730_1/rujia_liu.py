'''
Referências:
https://vjudge.net/problem/UVA-11991

'''

lista = [[] for _ in range(1000001)]

n, m = map(int, input().split())

data = list(map(int, input().split()))

for i in range(n):
    lista[data[i]].append(i+1)

ans = []
for i in range(m):
    k, v = map(int, input().split())
    ans.append(lista[v][k-1] if len(lista[v]) >= k else 0)

for a in ans:
    print(a)