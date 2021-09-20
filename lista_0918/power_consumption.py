n, p1, p2, p3, t1, t2 = map(int, input().split())

energy = 0
for i in range(n):
    l, r = map(int, input().split())
    if i == 0: last = l
    inactive = l - last
    if inactive > t2 + t1:
        energy += (inactive-t1-t2)*p3 +t2*p2 + t1*p1
    elif inactive > t1:
        energy += (inactive-t1)*p2 + t1*p1
    else:
        energy += inactive*p1
    energy += p1*(r-l)
    last = r

print(energy)