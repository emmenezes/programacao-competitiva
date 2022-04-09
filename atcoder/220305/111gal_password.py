from math import log, ceil


s = input()
tam = len(s)
q = int(input())
max2 = ceil(log(1000000000000000000/tam, 2))

print(max2)

for _ in range(q):
    t, k = map(int, input().split())
    if t > max2:
        
#     else:
#         passo = pow(2,t)
    