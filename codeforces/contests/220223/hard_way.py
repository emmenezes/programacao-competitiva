t = int(input())

for _ in range(t):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))

    if a[1] == b[1] and c[1] < a[1]:
        print(abs(b[0] - a[0]))
    elif a[1] == c[1] and b[1] < a[1]:
        print(abs(c[0] - a[0]))
    elif b[1] == c[1] and a[1] < b[1]:
        print(abs(b[0] - c[0]))
    else:
        print(0)
    