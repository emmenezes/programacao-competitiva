primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
          197, 199]

a, b, c, d = map(int, input().split())

Aoki = True
has_prime = False

for i in range(a, b+1):
    has_prime = False
    for j in range(c, d+1):
        s = i+j
        if s in primes:
            has_prime = True
            break
    if not has_prime:
        Aoki = False
        break

if Aoki:
    print("Aoki")
else:
    print("Takahashi")

