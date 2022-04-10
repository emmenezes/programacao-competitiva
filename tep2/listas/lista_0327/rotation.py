from math import acos, hypot, asin, pi, cos, sin

k = int(input())
x, y = map(int, input().split())
z = hypot(x, y)

k = k*pi/180

a = acos(x/z) 
b = asin(y/z)
if b < 0:
    b = 2*pi + b
    pb = [b, pi + abs(b - 2*pi)]
else:
    pb = [b, pi - b]
pa = [a, 2*pi - a]

if abs(pa[0] - pb[0]) < 0.1 or abs(pa[0] - pb[1]) < 0.1:
    k += pa[0]
else:
    k += pa[1]

x = z*cos(k)
y = z*sin(k)

# print(f"a: {pa[0]*180/pi}, {pa[1]*180/pi}")
# print(f"b: {pb[0]*180/pi}, {pb[1]*180/pi}")
# print(f"k: {k*180/pi}")
print(f"{x:.6f} {y:.6f}")