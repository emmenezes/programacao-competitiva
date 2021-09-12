n, m = map(int, input().split())

tvs = list(map(int, input().split()))

tvs = sorted(tvs)
tvs = tvs[0:m]

soma = 0
for tv in tvs:
    if tv < 0:
        soma += tv
    else:
        break

print(-soma)