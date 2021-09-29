'''
Referências:
https://codeforces.com/contest/13/problem/A
https://codeforces.com/blog/entry/364
'''

import math

A = int(input())

sum = 0
for i in range(2, A):
    d = A
    while (d >= i) :
        sum += d%i
        d //= i
    sum += d

A -= 2
gcd = math.gcd(A, sum)
print(f'{sum//gcd}/{A//gcd}')