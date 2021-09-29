n = int(input())

leaves = []

for _ in range(n):
    leaf = input()
    if leaf not in leaves:
        leaves.append(leaf)

print(len(leaves))
