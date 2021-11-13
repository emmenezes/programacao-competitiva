def resolve():
    pass

def check(n):
    done = True
    p = data[0][0]
    for i in range(n):
        for j in range(n):
            if data[i][j] != p:
                done = False
                break
        if not done:
            break
    
    return done

n = int(input())

data = []

for _ in range(n):
    data.append(input())

