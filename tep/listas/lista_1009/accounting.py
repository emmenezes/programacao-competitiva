import math


A, B, n = map(int, input().split())

if B == 0 and A == 0:
    print(1)
    quit()
if A == 0:
    print("No solution")
    quit()
if B%A != 0:
    print("No solution")
    quit()
if B == 0:
    print(0)
    quit()


p = B//A

sig = ""
if p < 0:
    sig = "-"
    p = abs(p)

if sig == "-" and n%2 == 0:
    print("No solution")
    quit()

X = math.ceil(p ** (1/n))

if X**n != p:
    print("No solution")
    quit()

print(f'{sig}{int(X)}')