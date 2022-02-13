from collections import Counter

l = []

n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if a[i]%2 == 0:
        l.append(2)
        a[i] //= 2
    
    j = 3
    while j <= a[i]:
        if a[i]%j == 0:
            l.append(j)
            a[i] //= j
        j += 2

cnt = Counter(l)
print(cnt.most_common(1)[0][0])