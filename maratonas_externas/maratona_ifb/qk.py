n = input()

ans = 0

for i in n:
    num = int(i)
    ans += num%3
    ans = ans%3

if ans == 0:
    print("Sim")
else:
    print("Nao")

