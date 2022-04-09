s = input()

r = 0
mr = 0
for sx in s:
    if sx == "R":
        r += 1
    else:
        if r > mr:
            mr = r
            r = 0
if r > mr:
    mr = r
    r = 0
print(mr)
