soma = input()
i = 0
while len(soma) != 1:
    soma = str(sum(int(digit) for digit in soma))
    i += 1

print(i)