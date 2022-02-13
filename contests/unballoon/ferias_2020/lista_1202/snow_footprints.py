# Ideias
# - É possível dizer que Alice pode começar de qualquer ponto no meio?

# n = int(input())
# s = input()

# s = ['.' for _ in range(n)]
# pos = int(input())

# while (True):
#     entry = input()

#     if entry == "L":
#         s[pos-1] = "L"
#         pos -= 1
#     elif entry == "R":
#         s[pos-1] = "R"
#         pos += 1
#     else:
#         s = ['.' for _ in range(n)]
#         pos = int(input())
#     print(*s)
        

n = int(input())
s = input()

pos_init = 0
pos_final = 0


if "R" in s and "L" in s:
    pos_init = s.index("R") + 1
    pos_final = s.index("L")
    print(f"{pos_init} {pos_final}")
elif "R" in s:
    s_rev = s[::-1]
    pos_init = s.index("R")+1
    pos_final = n - s_rev.index("R") + 1
    print(f"{pos_init} {pos_final}")
elif "L" in s:
    s_rev = s[::-1]
    pos_init = n - s_rev.index("L")
    pos_final = s.index("L")
    print(f"{pos_init} {pos_final}")
else:
    print("1 1")
