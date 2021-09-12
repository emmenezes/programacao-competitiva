n, m = map(int, input().split())

songs = n + m - 1
print(songs)

for i in range(m):
    print(1, i+1)

for i in range(1,n):
    print(i+1,1)