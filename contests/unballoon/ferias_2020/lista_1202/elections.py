n, m = map(int, input().split())
cand_n = [0 for _ in range(n)]

for _ in range(m):
    city = list(map(int, input().split()))
    cand_max = max(city)
    cand_n[city.index(cand_max)] += 1

cand_max = max(cand_n)
print(cand_n.index(cand_max)+1)