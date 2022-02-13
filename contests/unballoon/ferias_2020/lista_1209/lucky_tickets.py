n = int(input())
data = list(map(int, input().split()))
mult3 = [0, 0, 0]

for i in data:
    mult3[i%3] += 1

ans = mult3[0]>>1 
ans += min(mult3[1], mult3[2])
print(ans)