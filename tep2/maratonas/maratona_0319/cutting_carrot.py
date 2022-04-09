from math import sqrt

n, h = map(int, input().split())

A = h/2

res = []

for i in range(1, n):
    x = sqrt(i*h*h/n) 
    res.append(x)

print(*res)