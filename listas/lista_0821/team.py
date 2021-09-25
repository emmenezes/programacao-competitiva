n = int(input())
res = 0

for i in range (n):
    ques = list(map(int, input().split()))
    if (ques[0] + ques[1] + ques[2] >= 2):
        res += 1

print(res)