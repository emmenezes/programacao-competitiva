s = input()

if s[0] == "-":
    if len(s) == 2:
        print(-1)
    elif s[-1] == "0":
        print(s[:-1])
    else:
        s = int(s[:-1])-1
        print(s)
else:
    if len(s) == 1:
        print(0)
    else:
        print(s[:-1])