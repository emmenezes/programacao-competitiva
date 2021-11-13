n = int(input())
data = list(map(int, input().split()))

data = sorted(data)

fst = data[0]

for item in data[1:]:
    if item != fst:
        print(item)
        quit()

print("NO")
