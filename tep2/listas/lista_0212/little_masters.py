t = int(input())

for _ in range(t):
    x, y, R = map(int, input().split())
    r = (x*x + y*y)**0.5
    print(f"{R-r:.2f} {R+r:.2f}")
