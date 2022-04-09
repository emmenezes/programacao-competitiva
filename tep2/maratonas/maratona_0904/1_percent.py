y = int(input())
y -= 100

l = [100]
p = 0

while y > sum(l):
    l.append(l[-1]+100)
    p += 1

print('p ', p)

base = sum(l[:-1])
print(f"base {base}")

falta = y - base
print(f"falta {falta} {y} {base}")

taxa = l[-1]//100

dias = falta//taxa
print(f"dias {dias}")
if falta%taxa:
    dias += 1

res = p*100 + dias 

print(res)