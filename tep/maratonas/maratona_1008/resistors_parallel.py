import math

n = int(input())
a = list(map(int, input().split()))

lcm = a[0]
for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])

sum = 0
for i in range(len(a)):
    sum += lcm//a[i]

g = math.gcd(lcm, sum)
lcm, sum = lcm/g, sum/g

print(lcm/sum)