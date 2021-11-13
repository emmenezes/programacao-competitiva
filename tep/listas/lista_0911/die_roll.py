Y, W = map(int, input().split())

D = 7 - max(Y,W) 

if D == 6:
    print("1/1")
elif D == 5:
    print("5/6")
elif D == 4:
    print("2/3")
elif D == 3:
    print("1/2")
elif D == 2:
    print("1/3")
else:
    print("1/6")