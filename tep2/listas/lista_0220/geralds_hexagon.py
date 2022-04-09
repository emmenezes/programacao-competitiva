a, b, c, d, e, f = map(int, input().split())

if b >= a and b >= c:
    print((a+b+c)**2 - a**2 - c**2 - e**2)
else:
    print((b+c+d)**2 - b**2 - d**2 - f**2)
