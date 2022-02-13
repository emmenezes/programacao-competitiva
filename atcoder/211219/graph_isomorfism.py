n, m = map(int, input().split())

a = [[] for _ in range(n)]
cb = [[] for _ in range(n)]

for _ in range(m//2):
    am, bm = map(int, input().split())
    