t = int(input())

for _ in range(t):
    a, s = input().split()
    l = -len(a)
    i = -1
    ai = -1
    b = []

    while ai >= l:
        try:
            # print(s[i])
            t = int(s[i])
            if int(a[ai]) > t:
                i -= 1
                if s[i] != '1':
                    # print(s[i])
                    raise Exception
                t += 10
            b.insert(0, str(t - int(a[ai])))
            # print(a[ai], b[0], t)
            ai -= 1
            i -= 1
        except Exception as e:
            # print(e)
            b = ["-1"]
            i = -len(s) -1
            break

    l = -len(s)
    if i >= l:
        b.insert(0, s[:i+1])
    
    # print(b)
    b = "".join(b)
    print(b.lstrip("0"))

            