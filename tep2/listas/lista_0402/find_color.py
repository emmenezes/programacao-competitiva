x, y = map(int, input().split())

d = (x*x + y*y)**0.5

if d.is_integer() or x == 0 or y == 0:
    print("black")
else:
    if x * y > 0:
        if int(d)%2 == 0:
            print("black")
        else:
            print("white")
    else:
        if int(d)%2 == 0:
            print("white")
        else:
            print("black")

