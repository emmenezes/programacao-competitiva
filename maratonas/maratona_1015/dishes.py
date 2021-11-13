n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

b.insert(0, 0); c.insert(0, 0)

ans = 0
last = -1
actual = 0

for i in range(n):
    pos = a[actual]
    #print(last, pos, b[pos])
    if last + 1 == pos:
        ans += c[last]
    ans += b[pos]

    last = pos
    actual += 1

print(ans)