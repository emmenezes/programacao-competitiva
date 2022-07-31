t = int(input())

for _ in range(t):
    s = input()
    l = len(s)

    if l%2 == 1:
        print("NO")
    else:
        m = l//2
        e = True
        for i in range(m):
            if s[i] != s[m+i]:
                print("NO")
                e = False
                break
        if e:
            print("YES")
