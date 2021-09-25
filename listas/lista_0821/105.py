n = int(input())

if (n < 105):
    print(0)
else:
    res = 0
    for i in range(105,n+1,2):
        divisores = 1
        a = 1
        while a*2 <= i:
            if (i%a == 0):
                divisores += 1
            a += 1
        if (divisores == 8):
            res += 1
    print(res)