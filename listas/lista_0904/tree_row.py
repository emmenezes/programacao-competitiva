n, k = map(int, input().split())

a = list(map(int, input().split()))
dif = []

for i in range(n-1):
    dif.append(a[i+1]-a[i])

print(dif)
seq = []
tam = 0
loop = False
for i in range(len(dif)):
    # print(i, k, loop)
    if dif[i] == k and not loop:
        tam = 1
        inicio = i
        loop = True
    elif dif[i] == k:
        tam += 1
    elif loop:
        seq.append([tam, inicio, i])
        loop = False

print(seq)