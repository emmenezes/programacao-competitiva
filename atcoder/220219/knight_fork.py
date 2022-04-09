x1, y1, x2, y2 = map(int, input().split())

lat = [[-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2], [-2,-1]]

lat1 = []
lat2 = []
for x,y in lat:
    lat1.append([x+x1, y+y1])
    lat2.append([x+x2, y+y2])

if [1 for i in lat1 if i in lat2]:
    print("Yes")
else:
    print("No")