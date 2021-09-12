n = int(input())

ans = []

for i in range(n):
    t = int(input())
    if t <= 15:
        ans.append(0) 
    elif t <= 60:
        ans.append(10*(t-15))
    elif t <= 180:
        ans.append(450+8*(t-60))
    elif t <= 420:
        ans.append(1410+6*(t-180))
    else:
        ans.append(2850+2*(t-420))

for elem in ans:
    print("%.2f" % (elem/100))