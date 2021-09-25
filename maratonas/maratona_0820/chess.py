r1, c1, r2, c2 = map(int, input().split())

# Torre
rook =int(r1 != r2) + int(c1 != c2)

# Bispo
bishop = 0
if ((r1+c1)%2 == (r2+c2)%2):
    if (r1 == r2 and c1 == c2):
        bishop = 0
    elif ((r1-c1 == r2 -c2) or (r1 + c1 == r2 + c2)):
        bishop = 1
    else:
        bishop = 2


# Rei
king = 0
r, c = r2 - r1, c2 - c1

king = 0

while (r1 != r2 and c1 != c2):
    king += 1

    if r > 0:
        r1 += 1
    else:
        r1 -= 1
    if c > 0:
        c1 += 1
    else:
        c1 -= 1

king += abs(r1-r2) + abs(c1-c2)

print(rook, bishop, king)