# Ref: https://codeforces.com/contest/8/status/A

# s=input()
# a=input()
# b=input()
# r=a+'.*'+b
# print(r)
# import re
# print(['fantasy','forward','backward','both'][(re.search(r,s)!=None)+2*(re.search(r,s[::-1])!=None)])

# Ref: https://www.w3schools.com/python/python_regex.asp 

# s,x,y,t=input(),input(),input(),0
# e=s[::-1]
# if x in s:
#     q=s.index(x)+len(x)
#     if y in s[q:]:t+=1
# if x in e:
#     q=e.index(x)+len(x)
#     if y in e[q:]:t+=2
# print(["fantasy","forward","backward","both"][t])

# def f(a, b, c):
#     i, j = a.find(b), a.rfind(c)
#     return i != -1 and j != -1 and i + len(b) <= j
# a, b, c = input(), input(), input()
# print(('fantasy', 'backward', 'forward', 'both')[2 * f(a, b, c) + f(a[::-1], b, c)])

s,a,b,ans=input(),input(),input(),0
e = s[::-1]

if a in s:
    p = s.index(a) + len(a)
    if b in s[p:]: ans += 1
if a in e:
    p = e.index(a) + len(a)
    if b in e[p:]: ans += 2

print(["fantasy", "forward", "backward", "both"][ans])