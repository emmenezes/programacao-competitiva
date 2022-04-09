k = int(input())
s = input()
l = len(s)

if l <= k:
    print(s)
else:
    cs = s[0:k] + '...'
    print(cs)