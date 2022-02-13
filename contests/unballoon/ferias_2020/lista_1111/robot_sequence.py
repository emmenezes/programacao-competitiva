n = int(input())
pos = [0, 0]
pos_n = [None for _ in range(n)]
sol = 0
v = {
    'U': 1,
    'D': -1
}
h = {
    'R': 1,
    'L': -1
}
e = input()

for i in range(n):
    s = e[i]
    if s == 'U' or s == 'D':
        pos[1] += v[s]
    else:
        pos[0] += h[s]
    
    pos_n[i] = pos.copy()
    if pos == [0,0]:
        sol += 1

for i in range(n-1):
    for j in range(i+1, n):
        fin = [pos_n[j][0]-pos_n[i][0], pos_n[j][1]-pos_n[i][1]]
        if fin[0] == 0 and fin[1] == 0:
            sol += 1
        


print(sol)
# print(pos_n)