n, m = map(int, input().split())

groups = []

group = list(map(int, input().split()))
counter = 1
while group[0] == 0 and counter != m:
    group = list(map(int, input().split()))
    counter += 1
groups.append(group[1:])

for i in range(m-counter):
    group = list(map(int, input().split()))
    if group[0] != 0:
        number = -1
        for j in range(len(groups)):
            for k in range(group[0]):
                if group[k+1] in groups[j]:
                    number = j
                    break
            if number != -1:
                break
        if number != -1:
            groups[number].extend(group)
            groups[number] = list(dict.fromkeys(groups[number]))
        else:
            groups.append(group[1:])
        
friends = [1 for i in range(n+1)]

for i in range(len(groups)):
    for j in range(len(groups[i])):
        friends[groups[i][j]] = len(groups[i])

friends = friends[1:]
print(*friends, sep=' ')