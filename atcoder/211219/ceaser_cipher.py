# a =  97
# z = 122

S = input()
T = input()

comp = []

for i in range(len(S)):
    dif = ord(T[i]) - ord(S[i])
    if dif < 0:
        dif += 26
    comp.append(dif)

init_value = comp[0]
for value in comp[1:]:
    if value != init_value:
        print("No")
        quit()

print("Yes")
