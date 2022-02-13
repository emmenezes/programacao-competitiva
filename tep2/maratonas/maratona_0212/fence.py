n = int(input())

for _ in range(n):
    l = list(map(int, input().split()))
    print(int((l[1]**2 + (l[2] - l[0])**2)**0.5))