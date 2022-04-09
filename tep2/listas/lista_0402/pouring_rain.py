from math import pi

d, h, v, e = map(int, input().split())
r = d/2
vm = v/(pi*r*r)


if vm < e:
    print("NO")
else:
    print("YES")
    t = h/(vm-e)
    print(t)
