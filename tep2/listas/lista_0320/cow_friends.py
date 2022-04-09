t = int(input())

for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    if x in a:
        print(1)
    else:
        m = max(a)
        if m > x:
            print(2)
        else:
            if (x%m == 0):
                print(x//m)
            else:
                print(x//m + 1)