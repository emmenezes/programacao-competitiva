t = int(input())

for i in range(t):
    n = int(input())
    data = [x%2 for x in list(map(int, input().split()))]

    if (sum(data) != n//2 and sum(data) != (n+1)//2):
        print(-1)
        continue
    
    if n%2 == 0:
        side1, side2 = sum(data[:(n+1)//2]), sum(data[(n+1)//2:])
        if (abs(side1-side2) == 1):
            print(0)
        else:
            
            pass
    else:
        pass
    print("saida  ->  ", max(sum(data[:(n+1)//2]), sum(data[(n+1)//2:])))