a, x, y = map(int, input().split())

if (x == 0 or x == a or y == 0 or y == a):
    print(1)
elif ((x > 0 and x < a) and (y > 0 and y < a)):
    print(0)
else:
    print(2)