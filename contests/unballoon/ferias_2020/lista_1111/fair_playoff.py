t = int(input())

for _ in range(t):
    p = list(map(int, input().split()))
    p_sort = sorted(p)
    p_max = p_sort[2:]

    if p.index(p_max[0])//2 != p.index(p_max[1])//2:
        print("YES")
    else:
        print("NO")
