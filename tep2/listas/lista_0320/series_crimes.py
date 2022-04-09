n, m = map(int, input().split())

c = []

for i in range(n):
    line = input()
    for j in range(len(line)):
        if line[j] == "*":
            c.append([i,j])

ps =    [[c[0][0] , c[1][1]],
         [c[0][0] , c[2][1]],
         [c[1][0] , c[0][1]],
         [c[1][0] , c[2][1]],
         [c[2][0] , c[0][1]],
         [c[2][0] , c[1][1]],
        ]

for p in ps:
    if p not in c:
        print(p[0] + 1, p[1] + 1)
        quit()
    