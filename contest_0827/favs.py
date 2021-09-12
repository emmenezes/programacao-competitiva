n = int(input())

for i in range (n):
    a, b = map(int, input().split())
    if a + b == 0:
        print(0)
    elif a == b:
        print(1)
    elif (a+b)%2 == 0:
        print(2)
    else:
        print(-1)
