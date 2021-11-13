passwords = []

n = int(input())

for _ in range(n):
    word = [c for c in input()]
    word = set(word)
    # print(f"palavra {word}")
    has_letter = False
    for id, p in enumerate(passwords):
        # print(f"conjunto {p}")
        for letter in word:
            # print(f"letra {letter}")
            if letter in p:
                has_letter = True
                break
        if has_letter:
            passwords[id] = p.union(word)
            # print(passwords)
            break
    # print(f"status {has_letter}")
    if not has_letter:
        passwords.append(set(word))
    else:
        for i in range(len(passwords)-1, -1, -1):
            if i != id:
                l = passwords[id].intersection(passwords[i])
                if len(l) != 0:
                    passwords[id].union(passwords[i])
                    passwords.pop(i)
                    if i < id:
                        id -= 1
    # print(passwords)

print(len(passwords))