n = int(input())
data = [[id, y] for id, y in enumerate(list(map(int, input().split())))]

data = sorted(data, key=lambda x:-x[1])

ans = []

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1,n):
            if data[i][1] == data[j][1] + data[k][1]:
                ans = [data[i][0]+1, data[j][0]+1, data[k][0]+1]
                print(*ans)
                quit()
            if data[i][1] > data[j][1] + data[k][1]:
                break

print(-1)