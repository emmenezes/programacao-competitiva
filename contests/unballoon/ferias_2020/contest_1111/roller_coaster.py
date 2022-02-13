n, k = map(int, input().split())
h = list(map(int, input().split()))

t = 0
for hx in h:
    if hx >=k:
        t += 1

print(t)