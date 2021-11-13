n = int(input())
people = list(map(int, input().split()))
max_p = people.index(max(people))

hier = [1000001 for x in range(n)]

m = int(input())

for i in range(m):
    data = list(map(int, input().split()))
    if data[2] < hier[data[1]-1]:
        hier[data[1]-1] = data[2]

wo_sv =[i for i in hier if i == 1000001]

if len(wo_sv) > 1:
    print(-1)
else:
    hier = hier[:max_p] + hier[max_p+1:]
    cost = sum(hier)
    print(cost)