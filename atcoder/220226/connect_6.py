n = int(input())
s = []

for _ in range(n):
    s.append(input())

possivel = False
for i in range(n):
    for j in range(n):
        if s[i][j] == "#":
            # print("pontos", i, j)
            # Confere horizontal
            h = s[i][j+1:min(n,j+6)]
            # print(h)
            if h.count("#") >= 3:
                possivel = True
                break
            # Confere vertical
            v = [s[k][j] for k in range(i+1,min(n,i+6))]
            # print(v)
            if v.count("#") >= 3:
                possivel = True
                break
            # Confere diagonal direta
            d = min(n-j, n-i) - 1
            extra = min(i,n-1-j)
            dd = [s[i+m][j+m] for m in range(1,d)]
            # print("direta", dd)
            if dd.count("#") >= 5-min(extra, 2):
                possivel = True
                break
            # Confere diagonal inversa
            dc = min(n-i-1,j)+1
            extra = min(i,j)
            di = [s[i+m][j-m] for m in range(1,dc)]
            # print("inversa", di)
            if di.count("#") >= 5-min(extra,2):
                possivel = True
                break
    if possivel:
        break

if possivel:
    print("Yes")
else:
    print("No")
