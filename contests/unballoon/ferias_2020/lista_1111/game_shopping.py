n, m = map(int, input().split())

c = list(map(int, input().split()))
a = list(map(int, input().split()))
s = len(a)

i = 0
for cx in c:
    if a[i] >= cx:
        i += 1
    if i == s:
        break

print(i)