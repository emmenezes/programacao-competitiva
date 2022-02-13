t = int(input())

y0 = []
yh = []
x0 = []
xw = []

for _ in range(t):
    w, h = map(int, input().split())
    y0 = list(map(int, input().split()))
    yh = list(map(int, input().split()))
    x0 = list(map(int, input().split()))
    xw = list(map(int, input().split()))

    d_y0 = max(y0[1:]) - min(y0[1:])
    d_yh = max(yh[1:]) - min(yh[1:])
    d_x0 = max(x0[1:]) - min(x0[1:])
    d_xw = max(xw[1:]) - min(xw[1:])

    d_y = max(d_y0, d_yh)
    d_x = max(d_x0, d_xw)

    a1 = d_y*h
    a2 = d_x*w
    print(max(a1,a2))