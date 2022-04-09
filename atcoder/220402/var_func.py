from math import floor

n = int(input())

i, j = floor(n**(1/3)), 0
s, m = 0, 1000000000000000001

while n != m:
    s = i**3
    if s >= n:
        if s < m:
            m = s
        break
    for j in range(1,i+1):
        s = i**3 + i*i*j + i*j*j + j**3
        if s >= n and s < m:
            m = s
    i += 1

print(m)