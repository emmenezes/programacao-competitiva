n, m = map(int, input().split())

matches = []

for i in range(m):
    matches.append(list(map(int, input().split())))

# Depois faz um order na lista de acordo com o item 1
# E vai dando pop nos matches enquanto n > matches[-1][0]
# Ai quando não for é só pegar quantos puder