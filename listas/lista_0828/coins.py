n = int(input())
data = list(map(int, input().split()))

pos, neg = [], []

for num in data:
    if num < 0:
        neg.append(num)
    else:
        pos.append(num)

balanced = False if len(neg) % 2 else True

coins = 0

if balanced:
    for num in pos:
        coins += num -1 if num != 0 else 1
    for num in neg:
        coins += -num -1
else:
    for num in pos:
        coins += num -1 if num != 0 else 1
    for num in neg:
        coins += -num -1
    coins += 2

print(coins)