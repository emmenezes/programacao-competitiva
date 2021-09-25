teams = {}
# nome
# 0 pontos (+3 vitoria, +1 empate, 0 derrota)
# 1 gols marcados - gols sofridos
# 2 gols marcados

n = int(input())

for i in range(n):  teams[input()]= [0, 0, 0]

for i in range((n*n - n)//2):
    match, goals = input().split()
    match = match.split('-')
    goals = list(map(int, goals.split(':')))

    if goals[0] == goals[1]:
        teams[match[0]][0] += 1
        teams[match[0]][2] += goals[0]
        teams[match[1]][0] += 1
        teams[match[1]][2] += goals[0]
    elif goals[0] > goals[1]:
        teams[match[0]][0] += 3
        teams[match[0]][1] += goals[0] - goals[1]
        teams[match[0]][2] += goals[0]
        teams[match[1]][1] += goals[1] - goals[0]
        teams[match[1]][2] += goals[1]
    else:
        teams[match[0]][1] += goals[0] - goals[1]
        teams[match[0]][2] += goals[0]
        teams[match[1]][0] += 3
        teams[match[1]][1] += goals[1] - goals[0]
        teams[match[1]][2] += goals[1]

teams = list(teams.items())
teams = sorted(teams, key=lambda x: (-x[1][0], -x[1][1], -x[1][2]))
teams = sorted([team[0] for team in teams[:n//2]])

for team in teams:
    print(team)

