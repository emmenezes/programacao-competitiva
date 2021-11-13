n = int(input())
data = [0 for i in range(3002)]

lista = list(map(int, input().split()))
for i in range(n):
    data[lista[i]] = 1

for i in range(1, 3002):
    if data[i] == 0:
        print(i)
        quit()