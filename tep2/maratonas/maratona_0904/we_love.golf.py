k = int(input())
a, b = map(int, input().split())

r = a//k
if a%k == 0 and r:
    s = k*r
else:
    s = k*r + k

if s >= a and s <= b:
    print("OK")
else:
    print("NG")