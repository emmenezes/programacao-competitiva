import bisect

n, t = map(int, input().split())

houses = []
for i in range (n):
    x, a = input().split()
    x, a = float(x), int(a)/2
    houses.append([x,a])

houses = sorted(houses, key=lambda x: x[0])

places = 2
for i in range(n-1):
    house = houses[i][0] + houses[i][1]
    next_house = houses[i+1][0] - houses[i+1][1]

    dist = next_house - house

    if dist == t:
        places += 1
    elif dist > t:
        places += 2

print(places) 

#print(houses)