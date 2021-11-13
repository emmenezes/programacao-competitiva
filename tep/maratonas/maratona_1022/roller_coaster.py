n, k = map(int, input().split())
h = list(map(int, input().split()))

sum = 0
for hx in h:
    if hx >= k:  sum += 1

print(sum)