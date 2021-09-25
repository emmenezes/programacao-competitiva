n = int(input())

data = list(map(int, input().split()))

if sum(data)%2 == 1:
    print(0)
    quit()

sum_data = sum(data)//2
count = 0
partial_sum = 0

for el in data[:-1]:
    partial_sum += el
    if partial_sum == sum_data:     count += 1

print(count)