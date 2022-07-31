def n_e_primo(n):
    if n%2 == 0:
        return(1)

    for i in range(3, n, 2):
        if n%i == 0:
            return(1)
    
    return(0)

t = int(input())

for _ in range(t):
    n = int(input())
    data = list(map(int, input().split()))
    index = [x for x in range(1, n+1)]
    
    if n_e_primo(sum(data)):
        print(len(data))
        print(*index)
        continue
    
    res = False
    for j in range(n):
        soma = sum(data) - data[j]
        if n_e_primo(soma):
            index.pop(j)
            print(len(data)-1)
            print(*index)
            res = True
            break
    
    if res: continue

    for j in range(n-1):
        for k in range(j, n):
            soma = sum(data) - data[j] - data[k]
            if n_e_primo(soma):
                index.pop(k)
                index.pop(j)
                print(len(index))
                print(*index)
                res = True
                break
        if res: break
        
            


