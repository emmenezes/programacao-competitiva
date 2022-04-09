n = int(input())
x = list(map(int, input().split()))
x = [abs(i) for i in x]

man = sum(x,0)
euc = (sum([i*i for i in x],0))**0.5
cheb = max(x)

print(f"{man}\n{euc}\n{cheb}")

