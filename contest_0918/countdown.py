def countdown(number):
    sum = 0
    for num in number[:-1]:
        if num != "0":  sum += 1 + int(num)
    sum += int(number[-1])
    return sum

t = int(input())

for _ in range(t):
    _ = int(input())
    number = input()

    print(countdown(number))