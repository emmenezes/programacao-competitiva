n = int(input())

if n%2 == 1:
    print(n)
    quit()

n //= 2
while n%2 == 0:
    n //= 2

print(n)