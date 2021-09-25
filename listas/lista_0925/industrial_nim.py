n = int(input())

par = 0

for _ in range(n):
    x, m = map(int, input().split())
    x %= 2
    if x == 0 and m != 1:
        x = 1
    
    par += x
    par %= 2

    #print(par)

print("tolik" if par == 1 else "bolik")
