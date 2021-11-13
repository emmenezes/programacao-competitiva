'''
Referências:
- https://codeforces.com/blog/entry/557 
'''

n, t = map(int, input().split())

m = list(map(int, input().split()))

data = []
for _ in range(n):
    data.append(list(map(int, input().split())))

t %= 2*n

for i in range(t):
    m[0] = (data[i%n][0]*2 - m[0])
    m[1] = (data[i%n][1]*2 - m[1])

print(*m)
