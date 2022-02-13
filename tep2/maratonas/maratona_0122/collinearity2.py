n = int(input())

x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1,n):
            if (x[i] - x[j]) * (y[j] - y[k]) == (x[j] - x[k]) * (y[i] - y[j]):
                print("Yes")
                exit()

print("No")