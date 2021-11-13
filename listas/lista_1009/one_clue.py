K, X = map(int, input().split())

ans = [a for a in range(X-K+1, X+K)]

print(*ans)