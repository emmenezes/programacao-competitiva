n = int(input())

conf = [0 for _ in range(n)]
vistos = 0
a = input().split()
b = input().split()

while vistos != n:
    i = conf.index(0)
    conf[i] = 1
    atual = a[i]
    next = b.index(atual)
    vistos += 2
    while a.index(next) != atual:
        pass


