n, m = map(int, input().split())
data = []

for _ in range(n):
    data.append(list(map(int, input().split())))

if data[0][0] != 0:
    print("NO")
    quit()

maxi = data[0][1]
if maxi >= m:
    print("YES")
    quit()

for i in range(1, n):
    if maxi < data[i][0]:
        break
    else:
        maxi = max(maxi, data[i][1])
    
    if maxi >= m:
        print("YES")
        quit()

print("NO")