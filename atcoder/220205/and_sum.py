T = int(input())
min_value = 0

for _ in range(T):
    a,s = map(int, input().split())
    min_value = a << 1
    resto = ~a
    if min_value == s:
        print('Yes')
    elif min_value > s:
        print('No')
    else:
        s -= min_value
        and_value = resto & s
        if and_value == s:
            print('Yes')
        else:
            print('No')


