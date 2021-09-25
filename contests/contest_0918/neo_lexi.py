'''
Referência:
https://atcoder.jp/contests/abc219/tasks/abc219_c
'''

order = input()

dic = {}
i = 0
for letter in order:
    dic[letter] = i
    i += 1

n = int(input())

s = []
for _ in range(n): s.append(input())

s.sort(key=lambda val: dic[val[0]])

print(s)