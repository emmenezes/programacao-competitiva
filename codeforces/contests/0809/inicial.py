t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    if (k == 0):
        print(1)
    else:
        resposta = 2 ** (k*n - 1) + n%2
        print(resposta)
    