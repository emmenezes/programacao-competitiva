t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0
    x = list(map(int, input().split()))
    for i in range(n):
        ans |= x[i]
    print(ans)