def search_pair(n):
    pair = []
    for i in range(1,n):
        for j in range(i, n):
            d2 = i*i + j*j
            if d2 == n*n:
                pair.append([i,j])
            if d2 > n*n:
                break
        if pair != []:
            break
    return pair


a, b = map(int, input().split())

pair_a = search_pair(a)
pair_b = search_pair(b)

if not pair_a or not pair_b:
    print("NO")
else:
    print("YES")
    print(0, 0)
    print( pair_a[1], - pair_a[0])
    print( - pair_b[0], - pair_b[1])

