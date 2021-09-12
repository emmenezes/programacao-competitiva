def temperature (T, H):
    return T*100 - H*6

N = int(input())

T, A = map(int, input().split())
A *= 100

H_data = list(map(int, input().split()))

temp, place = 1000000, -1

for i in range(N):
    temp_H = temperature(T, H_data[i])
    if abs(temp_H - A) < temp:
        temp = abs(temp_H - A)
        place = i+ 1
    
print(temp, place)
