n = int(input())

data = []
for _ in range(4):
    line = input().split()
    line = [int(a, 16) for a in line]
    data.append(line)

ans = 0
for h in range(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                xor = data[0][h] ^ data[1][i] ^ data[2][j] ^ data[3][k]
                if xor == 0: ans += 1

print(ans)

