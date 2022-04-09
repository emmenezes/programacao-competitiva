n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ss = 0
for i in range(n):
    if a[i] == b[i]:
        ss +=1
        a[i] = 0
        b[i] = 0

sd = sum(1 for ax in a if (ax in b and ax != 0))

print(ss)
print(sd)
