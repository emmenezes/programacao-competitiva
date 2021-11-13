c = int(input())

backlog = []
for _ in range(c):
    entry = input()
    if entry[0] == "+":
        i = entry[2:]
        backlog.append(i)
    else:
        if backlog == []:
            print("Backlog vazio")
        else:
            o = backlog.pop()
            print(o)