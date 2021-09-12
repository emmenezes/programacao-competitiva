n, m = map(int, input().split())
seq = input()
canc = input()

ans = []

for i in range(n-len(canc)+1):
    if seq[i:i+len(canc)] == canc:
        ans.append(i)

if ans == []:
    print (-1)
else:
    print (*ans, sep=' ')