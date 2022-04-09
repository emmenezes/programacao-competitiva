def ball_time(a,b,c):
    delta = (b*b - 4*a*c)**0.5
    t1 = (-b + delta)/(2*a)
    t2 = (-b - delta)/(2*a)
    if t1 <= 0:
        return t2
    return t1

def someone_near(t):
    pass

state = {0: "foul", 1: "caught", 2: "safe"}
p = []
b = []
ans = []

np = int(input().split("=")[1])
for _ in range(np):
    p.append(list(map(int, input().split())))

nb = int(input().split("=")[1])
for _ in range(nb):
    b.append(list(map(int, input().split())))

for i in range(nb):
    t = ball_time(b[i][0],b[i][1],b[i][2])
    x = b[i][3]*t + b[i][4]
    y = b[i][5]*t + b[i][6]
    print(i+1, x, y, t)
    if x < 0 or y < 0:
        ans.append([i+1, 0, x, y])
        continue
    



