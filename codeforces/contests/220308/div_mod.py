t = int(input())

for _ in range(t):
    l, r, a = map(int, input().split())
    if r < a:
        s = r//a + r%a
    else:
        m = max((r//a)*a - 1, l)
        s = max(m//a + m%a, r//a + r%a, l//a + l%a)
    print(s)