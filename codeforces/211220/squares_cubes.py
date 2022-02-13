t = int(input())

for _ in range(t):
    n = int(input())

    square = int(n**(1/2))
    cube = int(n**(1/3))
    if n == 1000000000:
        cube += 1
    ind6 = int(n**(1/6))
    # print(square)
    # print(cube)
    # print(ind6)
    print(f"{square + cube - ind6}")