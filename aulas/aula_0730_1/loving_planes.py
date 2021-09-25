'''
Referência:
https://codeforces.com/problemset/problem/939/A
https://codeforces.com/blog/entry/57892
'''

n = int(input())
love = list(map(int, input().split()))

ans = "NO"
for i in range(n):
    first_love = love[love[i]-1]
    second_love = love[first_love-1]

    if second_love == i + 1:
        ans = "YES"
        break

print(ans)