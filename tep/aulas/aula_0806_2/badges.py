'''
Referência:
https://codeforces.com/problemset/problem/1020/B
'''

n = int(input())

students = [0]
students += list(map(int, input().split()))

guilties = []
for i in range(1,n+1):
    reported = [1 for _ in range(n+1)]
    reported[i] = 0
    j = students[i]
    while (reported[j]):
        reported[j] = 0
        j = students[j]
    guilties.append(j)

print(*guilties)
        


