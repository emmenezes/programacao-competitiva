primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
          101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193,
          197, 199]

a, b, c, d = map(int, input().split())
e = d - c + 1

Aoki = False

i = 0
p = a[i]
while p <= b + d:
    p = a[i]
    if p < a + c:
        i += 1
    else:
        dist = a[i+1] - p + 1
        if dist >= e:
            Aoki = True
            break
        else:
            i += 1

if Aoki:
    print("Aoki")
else:
    print("Takahashi")

