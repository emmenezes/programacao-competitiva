n = int(input())

if n%2 == 1:
    print(-1)
    quit()

ans = []
for i in range(n//2):
    ans.append(i*2+2)
    ans.append(i*2+1)

print(*ans, sep=" ")