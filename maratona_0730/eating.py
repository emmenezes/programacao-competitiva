D, N = input().split()

D, N = int(D), int(N)

if (N == 100):
    print(101 * (100**D))
else:
    print(N * (100**D))