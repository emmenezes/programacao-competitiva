n, d = map(int, input().split())

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    b = x - y
    if b >= -d and b <= d:
        b = x + y
        if b >= d and b <= (2*n-d):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")