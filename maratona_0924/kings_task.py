n = int(input())
data = list(map(int, input().split()))

while (True):
    if (input() == "1"):
        for i in range(n):
            data[i*2], data[i*2+1] = data[i*2+1], data[i*2]
    else:
        for i in range(n):
            data[i], data[i+n] = data[i+n], data[i]
    print(data)