N, M, X, Y = map(int, input().split())
data_x = list(map(int, input().split()))
data_y = list(map(int, input().split()))

data_x.append(X)
data_y.append(Y)

max_x = max(data_x)
min_y = min(data_y)

if (max_x < min_y):
    print("No War")
else:
    print("War")