from cmath import pi


a1, a2, a3 = map(int, input().split())

a = a1*a2*a3
a = int(a**0.5)

l1 = a//(a1)
l2 = a//(a2)
l3 = a//(a3)

print(4*(l1+l2+l3))