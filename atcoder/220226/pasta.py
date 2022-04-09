n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for bx in b:
    if bx in a:
        a.remove(bx)
    else:
        print("No")
        quit()

print("Yes")