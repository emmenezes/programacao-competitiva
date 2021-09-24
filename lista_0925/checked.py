n, m = map(int, input().split())

data = []
ll = lc = -1
fl, fc = n +1, m+1

for i in range(n):
    line = input()
    data.append(line)
    for id, square in enumerate(line):
        if square == "*":
            if id < fc:
                fc = id
            if i < fl:
                fl = i
            if id > lc:
                lc = id
            if i > ll:
                ll = i

for i in range(fl,ll+1):
    print(*data[i][fc:lc+1], sep='')

#print(fl, ll)
#print(fc, lc)
        