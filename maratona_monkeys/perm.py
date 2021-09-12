n = int(input())
data = list(map(int, input().split()))

sorted_data = sorted(data)
sorted_data2 = sorted_data.copy()
# print(sorted_data)

index_data = []
for item in data:
    index = sorted_data.index(item)
    index_data.append(index)
    sorted_data[index] = -1
# print(index_data)

# print(sorted_data2)
best_perm = []
for item in index_data:
    best_perm.append(sorted_data2[n-1-item])
print(*best_perm, sep=" ")