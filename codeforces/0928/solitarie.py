t = int(input())

for _ in range(t):
    s = input()
    Bs = 0
    for i in s: 
        if i == "B": Bs += 1
    if len(s)/2 == Bs:
        print("YES")
    else:
        print("NO")