t = input()
n = len(t)

big = 0
substr = [[] for i in range(n)]

count = 0
for i in range(0,n):
    for j in range(0,i-big+1):
        count += 1
        sub = t[j:i+1]
        size = i - j
        if sub in substr[size]:
            big = size +1
        else:
            substr[size].append(sub)
    #print(substr)

#print(count)
if big == 0:
    print(0)
else:
    print(big)