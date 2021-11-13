def resolve(k):

f = []
n, m  = map(int, input().split())
data_c = [0 for _ in range(n+1)]
vis = [0 for _ in range(n+1)]
for _ in range(m):
    data_m = [map(int, input().split())]

c1 = int(input())
if c1 != 0:
    c = [map(int, input().split())]

    for i in c:
        data_c[c] = 1

c2 = int(input())
if c1 == 0 and c2 != 0: f = c[0]
c = [map(int, input().split())]
for i in c:
    data_c[c] = 2

if c1 == 0 and c2 == 0: f = 0



