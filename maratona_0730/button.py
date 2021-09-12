import math

n, m = input().split()
n, m = int(n), int(m)

if (m < n):
    print (n - m)
else:
    a = (m//n + m - n)
    b = math.floor(math.log2(m)/2) + n - m//math.floor(math.log2(m)/2)
    c = math.floor(math.log2(m)/2)
    print(a, b, c)