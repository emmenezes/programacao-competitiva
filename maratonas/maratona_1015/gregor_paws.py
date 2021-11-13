t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    enemy = list(input())
    gregor = list(input())
    if gregor[0] == "1":
        if enemy[0] == "0": ans +=1
        elif enemy[1] == "1":
            ans += 1
            enemy[1] = "2"
    if gregor[-1] == "1":
        if enemy[-1] == "0": ans +=1
        elif enemy[-2] == "1":
            ans += 1
            enemy[-2] = "1"
    for i in range(1,n-1):
        if gregor[i] == "1":
            if enemy[i] == "0": ans += 1
            elif enemy[i-1] == "1":
                ans += 1
                enemy[i+1] = "2"    
            elif enemy[i+1] == "1":
                ans += 1
                enemy[i+1] = "2"
    print(ans)
            