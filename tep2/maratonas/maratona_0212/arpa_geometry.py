ax, ay, bx, by, cx, cy = map(int, input().split())

dab = (ax-bx)**2 + (ay-by)**2
dbc = (cx-bx)**2 + (cy-by)**2

if dab == dbc:
    if (ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)):
        print("Yes")
    else:
        print("No")
else:
    print("No")