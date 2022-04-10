n = int(input())
a = list(map(int, input().split()))

s = 0
u = 0
for i in range(1, n):
    if (a[i] == 2 and a[i-1] == 3) or (a[i] == 3 and a[i-1] == 2):
        s = -1
        break
    else:
        if a[i] == 2 or a[i-1] == 2:
            if u == 3:
                s += 2
            else:
                s += 3
            u = 2
        else:
            s+= 4
            u = 3

if s > 0:
    print(f"Finite\n{s}")
else:
    print("Infinite")