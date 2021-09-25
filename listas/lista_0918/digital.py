n = int(input())

gift = 0
for _ in range(n):
    x, u = input().split()
    if u == "BTC":
        gift += 380000*float(x)
    else:
        gift += float(x)

print(gift)
