from math import sqrt, ceil

n = int(input())

l = ceil(sqrt(n))

c = l

while ((c-1)*l >= n):
    c -= 1

# print(c, l)
print(2*(c+l))