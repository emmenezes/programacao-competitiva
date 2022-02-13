H, M = map(int, input().split(":"))

h = (H%12) + M/60
m = M

print(f"{h*30} {m*6}")