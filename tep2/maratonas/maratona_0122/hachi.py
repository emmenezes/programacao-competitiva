from itertools import permutations

s = input()

if len(s) <= 2:
    if int(s)%8 == 0 or int(s[::-1])%8 == 0:
        print("Yes")
    else:
        print("No")
else:
    n = [sx for sx in s]
    temp = permutations(n, 3)
    for t in list(temp):
        if int(t[0]+t[1]+t[2])%8 == 0:
            print("Yes")
            exit()
    print("No")
    