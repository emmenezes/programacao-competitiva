n = int(input())
a = list(map(int, input().split()))

o = [0] * n

for i in range(n):
	o[a[i]-1] = i+1

print(*o, sep=' ')