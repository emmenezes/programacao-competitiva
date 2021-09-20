s = ['']

for _ in range(3): s.append(input())

t = input()

o = ''
for i in t:
    n = int(i)
    o += s[n]

print(o)