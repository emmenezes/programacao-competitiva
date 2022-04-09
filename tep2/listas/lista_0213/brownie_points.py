n = int(input())
stan = 0
ollie = 0
brownies = []


for _ in range(n//2):
    brownies.append(list(map(int, input().split())))

mid_brownie = list(map(int, input().split()))

for _ in range(n//2):
    brownie_x, brownie_y = map(int, input().split())
    if brownie_x != mid_brownie[0] and brownie_y != mid_brownie[1]:
        if (brownie_x > mid_brownie[0] and brownie_y > mid_brownie[1]) or (brownie_x < mid_brownie[0] and brownie_y < mid_brownie[1]):
            stan += 1
        else:
            ollie +=1

input()

for brownie in brownies:
    if brownie[0] != mid_brownie[0] and brownie[1] != mid_brownie[1]:
        if (brownie[0] > mid_brownie[0] and brownie[1] > mid_brownie[1]) or (brownie[0] < mid_brownie[0] and brownie[1] < mid_brownie[1]):
            stan += 1
        else:
            ollie +=1

print(f"{stan} {ollie}")