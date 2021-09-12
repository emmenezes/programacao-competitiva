min = 1000

n = input()

if len(n) < 3:
    n = int(n)
    print(abs(753-n))
    quit()

for i in range (len(n)-2):
    num = int(n[i:i+3])
    if abs(753-num) < min:
        min = abs(753-num)

print(min)