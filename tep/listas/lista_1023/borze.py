code = input()

i = 0; ans = ""

while i < len(code):
    if i+1 == len(code):
        ans += '0'
    elif code[i] == '.':
        ans += '0'
    elif code[i+1] == '.':
        ans += '1'
        i += 1
    else:
        ans += '2'
        i += 1
    i += 1

print(ans)
