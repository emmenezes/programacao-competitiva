def maior_fat(n):
    lst = []
    k = 1
    f = 1
    while f <= n:
        lst.append(f)
        k += 1
        f *= k
    return lst[::-1]

def conta_bit(n):
    w = 0
    while (n):
        w += 1
        n &= n - 1
    return w

t = int(input())

for _ in range(t):
    n = int(input())
    res = conta_bit(n)

    fat = maior_fat(n)
    for i in range(0, len(fat)):
        n -= fat[i]
        if n >= 0:
            temp_res = i + 1 + conta_bit(n)
            if temp_res < res:
                res = temp_res
    
    print(res)
    
