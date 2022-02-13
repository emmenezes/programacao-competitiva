from math import gcd


n, m, k = map(int, input().split())

if gcd(n,k) != 1:
    a = [0,0]
    b = [0,m]
    c = [2*n//k,0]
elif gcd(m,k) != 1:
    a = [0,0]
    b = [0,2*m//k]
    c = [n,0]
else:
    print("NO")
    exit()

print("YES")
print(*a)
print(*b)
print(*c)

