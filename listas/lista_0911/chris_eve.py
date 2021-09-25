N = int(input())

p = []
max = 0

for i in range(N):
    pi = int(input())
    p.append(pi)
    if pi > max:
        max = pi

ans = sum(p) - max//2

print(ans)
