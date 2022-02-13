n = input()
l = [int(i)%3 for i in n]
size = len(l)
l = [i for i in l if i != 0]

if l == []:
    print(0)
    exit()

count = [0,0,0]

for i in l:
    if i == 1:
        count[1] += 1
    else:
        count[2] += 1

count[1] %= 3
count[2] %= 3

if count[2] == count[1]:
    print(0)
else:
    res = abs(count[1] - count[2])
    print(count)
    if res == size:
        print(-1)
    else:
        print(res)

