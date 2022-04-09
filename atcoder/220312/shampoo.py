v, a, b, c = map(int, input().split())
total = a + b + c
v %= total

s = [a, b, c]
d = {0: 'F',
     1: 'M',
     2: 'T'}

pos = 0
while (v >= 0):
    v -= s[pos]
    pos = (pos+1)%3

pos = (pos+2)%3
print(d[pos])