s = input()

t = 0
for sx in s:
    t  += int(sx)

if (t%9 == 0):
    print("Yes")
else:
    print("No")