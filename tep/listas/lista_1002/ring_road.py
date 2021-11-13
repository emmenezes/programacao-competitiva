n = int(input())

data = [[] for _ in range(n+1)]

for _ in range(n):
    road = list(map(int, input().split()))
    data[road[0]].append([road[1], 0])
    data[road[1]].append([road[0], road[2]])

    