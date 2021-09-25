n, m = map(int, input().split())

matches = []

for i in range(m):
    matches.append(list(map(int, input().split())))

order_matches = sorted(matches, key=lambda x:x[1])

sum_matches = 0

while n != 0 and len(order_matches) != 0:
    last = order_matches.pop()
    if n > last[0]:
        n -= last[0]
        sum_matches += last[0]*last[1]
    else:
        sum_matches += last[1]*n
        n = 0

print(sum_matches)

# Depois faz um order na lista de acordo com o item 1
# E vai dando pop nos matches enquanto n > matches[-1][0]
# Ai quando não for é só pegar quantos puder