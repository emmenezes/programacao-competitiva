t = int(input())

for _ in range(t):
    x1, p1 = map(int, input().split())
    x2, p2 = map(int, input().split())

    while x1 >= 10:
        x1 /= 10
        p1 += 1
    
    while x2 >= 10:
        x2 /= 10
        p2 += 1

    if x1 == x2 and p1 == p2:
        print("=")
    elif p1 == p2:
        if x1 > x2:
            print(">")
        else:
            print("<")
    elif p1 > p2:
        print(">")
    else:
        print("<")