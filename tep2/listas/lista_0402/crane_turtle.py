x, y = map(int, input().split())

c = (4*x-y)/2
t = (y-2*x)/2

if c >= 0 and t >= 0 and c.is_integer() and t.is_integer():
    print("Yes")
else:
    print("No")