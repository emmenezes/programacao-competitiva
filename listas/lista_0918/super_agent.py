data = []

for i in range(3):
    line = input()
    data.append(line)

if data[0][0] != data[2][2] or data[0][1] != data[2][1] or data[0][2] != data[2][0] or data[1][0] != data[1][2]:
    print("NO")
else:   print("YES")