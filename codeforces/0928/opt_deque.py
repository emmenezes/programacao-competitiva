t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))

    new_data = [data[0]]
    for item in data[1:]:
        if item <= new_data[0]:
            new_data.insert(0,item)
        else:
            new_data.append(item)

    order = 0
    print(new_data)
    for i in range(1,n):
        for j in range(i):
            if new_data[i] < new_data[j]:
                new_data[i], new_data[j] = new_data[j], new_data[i]
                order += 1
                break
    print(new_data )
    print(order)