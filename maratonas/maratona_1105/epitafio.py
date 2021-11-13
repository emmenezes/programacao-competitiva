n, r = map(int, input().split())

for _ in range(r):
    data = input()

print(n*(n-1)//2 - r)

