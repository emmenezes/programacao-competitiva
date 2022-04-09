t = int(input())

for _ in range(t):
    a = int(input())

    i = 3
    ang = 180 - 360/3
    exists = False
    if ang == a:
        print("YES")
        continue
    while ang < a:
        i += 1
        ang = 180 - 360/i
        if ang == a:
            exists = True
            break
    if exists:
        print("YES")
    else:
        print("NO")