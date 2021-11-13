def color(id, data):
    s = len(data)

    if id == s:
        data[id-1] = "B"
        id = id - 1

    stat = data[id]
    for i in range(id-1, -1, -1):
        if data[i] == "?":
            if stat == "B":
                data[i] = "R"
                stat = "R"
            else:
                data[i] = "B"
                stat = "B"
        else:
            break

    stat = data[id]
    for i in range(id+1, s):
        if data[i] == "?":
            if stat == "B":
                data[i] = "R"
                stat = "R"
            else:
                data[i] = "B"
                stat = "B"
        else:
            break
    
    return data


t = int(input())

for _ in range(t):
    n = int(input())
    data = [c for c in input()]

    if n == 1 and data == "?":
        print("B")
        pass

    has_any_letter = False
    for i in range(n):
        if data[i] != "?":
            data = color(i, data)
            has_any_letter = True
    
    if not has_any_letter:
        data = color(n, data)
    
    print(*data, sep='')
