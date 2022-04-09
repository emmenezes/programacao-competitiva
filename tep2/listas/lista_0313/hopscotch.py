a, x, y = map(int, input().split())

if (y%a == 0):
    print(-1)
else:
    if (y > a):
        l = y//a + 1
        if (l%2 == 0):
            if (x <= -a/2) or (x >= a/2):
                print(-1)
            else:
                pos = 2 + (l//2-1)*3
                print(pos)
        else:
            if (x <= -a) or (x >= a) or (x == 0):
                print(-1)
            else:
                pos = 2 + 3*((l-1)//2-1)
                if (x < 0):
                    print(pos + 1)
                else:
                    print(pos + 2)

    else:
        if (x <= -a/2) or (x >= a/2):
            print(-1)
        else:
            print(1)