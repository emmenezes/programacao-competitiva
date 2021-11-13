t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))

    new_data = [data[0]]
    for item in data[1:]:
        if item < new_data[0]:
            new_data.insert(0,item)
        else:
            new_data.append(item)
    
    print(*new_data)