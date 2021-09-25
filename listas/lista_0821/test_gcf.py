from lcm_3 import resolve
import math

for i in range (99996,1000000,6):
    res = resolve(i)
    if (math.gcd(res[1], res[2]) != 1):
        print(res[0],res[1],res[2], math.gcd(res[1], res[2]))
        break