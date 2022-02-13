n = int(input())
a = list(map(int, input().split()))

pedacos = [[0,360]]
corte = 0

for i in range(n):
    corte = (corte+a[i])%360
    for j in range(len(pedacos)):
        if pedacos[j][0] < corte and pedacos[j][1] > corte:
            borda_inf = pedacos[j][0]
            pedacos[j][0] = corte
            pedacos.insert(j,[borda_inf,corte])

max_pedaco = 0
for p_inf,p_sup in pedacos:
    if p_sup - p_inf > max_pedaco:
        max_pedaco = p_sup - p_inf

print(max_pedaco)
