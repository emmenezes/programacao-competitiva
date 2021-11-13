import math

x, y, a, b = map(int, input().split())

d = math.gcd(a, b)
a, b = a//d, b//d

if x < a or y < b:  
    print("0 0")
    quit()

ra = x//a
rb = y//b

r = min(ra, rb)
print(r*a, r*b)