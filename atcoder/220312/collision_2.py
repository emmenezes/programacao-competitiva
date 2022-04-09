n = int(input())
coord = []

for i in range(n):
    c = list(map(int, input().split()))
    c.append(i)
    coord.append(c)

s = input()

coord = sorted(coord, key=lambda x: (x[1], x[0]))
collision = 0

l = 0
r = 1
while l < n-1 and r < n:
    while s[coord[l][2]] == "L" and l < n-1:
        # print(l, r, "A")
        l += 1
        r += 1
        if coord[l][1] != coord[r][1]:
            # print(l, r, "B")
            l = r
            r = l + 1
            continue
    if r < n and coord[l][1] == coord[r][1]:
        while r < n and s[coord[r][2]] == "R":
            # print(l, r, "C")
            r += 1
            if r < n and coord[l][1] != coord[r][1]:
                # print(l, r, "D")
                l = r
                r = l + 1
                break
    else:
        # print(l, r, "E")
        l = r
        r = l + 1
    if r < n and s[coord[r][2]] == "L" and s[coord[l][2]] == "R":
        print("Yes")
        quit()

print("No")