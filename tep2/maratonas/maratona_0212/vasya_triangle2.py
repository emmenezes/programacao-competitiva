from math import gcd


n, m, k = map(int, input().split())

if n%k == 0:
    a = [0,0]
    b = [0,m]
    c = [2*n//k,0]
elif m%k == 0:
    a = [0,0]
    b = [0,2*m//k]
    c = [n,0]
elif gcd(n,k) != 1 and gcd(m,k) != 1:
    j = k
    k = k//gcd(n,k)
    if m%k == 0:
        a = [0,0]
        b = [0, 2*m//k]
        c = [n//gcd(n,k), 0]
    else:
        print("NO")
        exit()    
else:
    print("NO")
    exit()

print("YES")
print(*a)
print(*b)
print(*c)

