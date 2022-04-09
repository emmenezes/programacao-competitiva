n = int(input())
l = list(map(int, input().split()))

l.sort()

s = 0
for i in range(n-2):
    for j in range(i+1,n-1):
        if l[i] == l[j]:
            continue
        for k in range(j+1,n):
            if l[j] == l[k]:
                continue
            if l[k] < l[i] + l[j]:
                s += 1
            else:
                break

print(s)
