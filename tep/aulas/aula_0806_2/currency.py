'''
Referência:
https://codeforces.com/problemset/problem/508/B
'''

n = input()

odd_pos = -1
odd_value = "a"
odds = False

if n[-1] in "02468":
    pass
else:
    for i in len(n):
        if n[i] in "02468" and n[i] > odd_value:
            odd_pos = i
            odd_value = n[i]
            odds = True

