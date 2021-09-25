d, sumTime = map(int, input().split())
time = []

for i in range (d):
    time.append(list(map(int, input().split())))

# print(time)

minPossible, maxPossible = 0, 0
final = []

for i in range(d):
    minPossible += time[i][0]
    maxPossible += time[i][1]
    final.append(time[i][0])

if (sumTime > maxPossible or sumTime < minPossible):
    print("NO")
    quit()

j = 0
while (sum(final) != sumTime):
    # print(sum(final), time[j][0], time[j][1])
    for i in range(time[j][0], time[j][1]):
        final[j] += 1
        if (sum(final) == sumTime):
            break
    j += 1 

print("YES")
print(*final, sep = " ")