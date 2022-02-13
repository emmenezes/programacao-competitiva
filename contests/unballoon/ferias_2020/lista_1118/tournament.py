n = int(input())
p = []      # players
c = {}      # counter
m = []      # matches

for i in range((n*(n-1))//2 - 1):
    r = list(map(int, input().split()))
    if r[0] in p:
        c[r[0]] += 1
    else:
        p.append(r[0])
        c.update({r[0]: 1})
    if r[1] in p:
        c[r[1]] += 1
    else:
        p.append(r[1])
        c.update({r[1]: 1})
    m.append(r)

s = []      # missing player

for key, value in c.items():
    if value == n - 2:
        s.append(key)
    if len(s) == 2:
        break

for 


print(*m)

