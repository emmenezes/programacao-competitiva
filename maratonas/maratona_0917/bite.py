n, l = map(int, input().split())

pie = [l + i - 1 for i in range(1,n+1)]
pie2 = [abs(apple) for apple in pie]
print(sum(pie) - pie[pie2.index(min(pie2))])