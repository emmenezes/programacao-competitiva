from math import gcd

a, b = map(int, input().split())

d = gcd(a, b)

divs = []
while d%2 == 0:
    divs.append(2)
    d //= 2

i = 3
while i*i <= d:
    if d%i == 0:
        divs.append(i)
        d //= i
    else:
        i += 2
if d != 1:
    divs.append(d)

# print(divs)

divs = set(divs)
if 1 in divs:
    print(len(divs))
else:
    print(len(divs) + 1)

