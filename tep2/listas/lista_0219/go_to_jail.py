n = int(input())

count = 0
triplet = False
for _ in range(n):
    a, b = map(int, input().split())
    if a == b:
        count += 1
    else:
        count = 0
    if count == 3:
        triplet = True

if triplet:
    print("Yes")
else:
    print("No")
