def count_pairs (a, b, k):
    counter = 0
    actual_a, actual_b = 0,0
    for i in range(k):
        actual_a = a[i]
        actual_b = b[i]
        for j in range(i+1, k):
            if actual_a != a[j] and actual_b != b[j]:
                counter += 1
    return (counter)

t = int(input())

for _ in range(t):
    a, b, k = map(int, input().split())
    a = input().split()
    b = input().split()
    pairs = []

    for i in range(k):
        pairs.append([a[k], b[k]])

    if k < 2:
        print(0)
    else:
        print(count_pairs(a,b,k))

