a = input()

r = list(map(int, input().split()))
g = list(map(int, input().split()))
b = list(map(int, input().split()))

area = 0

while (len(r)+len(g)+len(b) > 1):
    max_r = max(r)
    max_g = max(b)
    max_b = max(g)

    
    
