n = int(input())

cake = 4
donut = 7

def resolve(n, anterior, atual):
    if (n == atual):
        return ("Yes")
    if (n < atual):
        resolve(n)

if (n%4 == 0 or n%7 == 0):
    print("Yes")
else:
    print(resolve(n, 0, 0))
