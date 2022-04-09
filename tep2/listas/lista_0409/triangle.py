def dist(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2

def check_tri(l):
    l.sort()
    if l[0] == 0:
        return False
    if l[0] + l[1] == l[2]:
        return True
    return False

p = [[0,0], [0,0], [0,0]]
p[0][0], p[0][1], p[1][0], p[1][1], p[2][0], p[2][1] = map(int, input().split())

if check_tri([dist(p[0], p[1]), dist(p[0], p[2]), dist(p[2], p[1])]):
    print('RIGHT')
else:
    for i in range(3):
        for j in [[0,1], [1,-1], [-1,-1], [-1,1]]:
            p[i][0] += j[0]
            p[i][1] += j[1]
            if check_tri([dist(p[0], p[1]), dist(p[0], p[2]), dist(p[2], p[1])]):
                print("ALMOST")
                quit()
        p[i][0] += 1
    print("NEITHER")



