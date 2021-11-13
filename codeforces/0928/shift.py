t = int(input())
 
for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    data_sorted = sorted(data)
 
    #print(data)
    #print(data_sorted)
 
    ans = []
    for i in range(n):
        if data[i] != data_sorted[i]:
            index = data.index(data_sorted[i], i)
            temp = data[index]
            t = index - i
            #print(i, data[i], data_sorted[i], temp, index)
            for j in range(index, i, -1):
                data[j] = data[j-1]
            data[i] = temp
            ans.append([i+1, index+1, t])
    
    print(len(ans))
    if len(ans) == 0:
        print(0)
        print('0 0 0')
    else:
        for a in ans:
            print(*a)
 
'''
Output:
k - número de ações para ordernar a lista
l r d - ação de deslocamento
 
'''