from math import gcd

a, b = map(int, input().split())

g = gcd(a,b)

if g == 1:
    print("NO")
    quit()

pair = []
for i in range(1,g):
    for j in range(i, g):
        d2 = i*i + j*j
        if d2 == g*g:
            pair.append(i)
            pair.append(j)
            break
        if d2 > g*g:
            break
    if pair != []:
        break

if pair:
    print("YES") 

    pa = [a//g * pair[1], -a//g * pair[0]] 
    pb = [-b//g * pair[0], -b//g * pair[1]]

    if (pa[0] == pb[0]) or (pa[1] == pb[1]):
        pa = [-pa[1], pa[0]]
        pb = [pb[1], -pb[0]]

    print(0,0)
    print(*pa)
    print(*pb)
else:
    print("NO")