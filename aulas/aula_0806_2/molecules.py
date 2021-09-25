'''
Referência:
https://codeforces.com/contest/344/problem/B
https://codeforces.com/blog/entry/8860
'''

a,b,c=map(int,input().split())
if(a+b<c)|(b+c<a)|(a+c<b)|((a+b+c)%2==1):
	print("Impossible")
else:
	print((+a+b-c)//2,(-a+b+c)//2,(+a-b+c)//2)