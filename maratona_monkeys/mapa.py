n = int(input())
data = list(map(int, input().split()))
altura = 1000000000
ponto = 0

for i in range(1, n-1):
    if data[i] < data[i-1] and data[i] < data[i+1] and data[i] < altura:
        altura = data[i]
        ponto = i + 1

print(ponto)