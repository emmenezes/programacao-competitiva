t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    montanha = list(map(int, input().split()))

    picos = [0]
    for i in range(1,n-1):
        if montanha[i] > montanha[i-1] and montanha[i] > montanha[i+1]:
            picos.append(1)
        else:
            picos.append(0)
    picos.append(0)
    # print(*picos)
    p = sum(picos[1:k-1])
    max_p = p
    pos = 0
    # print(f"De 0 até {k-1} há {p} picos")
    for i in range(1, n-k+1):
        p += picos[k+i-2] - picos[i]
        # print(f"De {i} até {k+i-1} há {p} picos, adicionou-se {picos[k+i-2]} e retirou-se {picos[i]}")
        if p > max_p:
            max_p = p
            pos = i
    
    print(f"{max_p + 1} {pos + 1}")


    