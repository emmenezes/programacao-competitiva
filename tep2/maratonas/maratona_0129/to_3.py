n = input()

d = [int(i)%3 for i in n]
size = len(d)
l = [i for i in d if i != 0]
s = sum(d, 0)
r = s%3

if r == 0:
    print(0)
    exit()
elif r in d and size != 1:
    print(1)
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
    # print(res, size)
    if res == size:
        print(-1)
    else:
        print(res)

