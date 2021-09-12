N = int(input())

T, A = map(int, input().split())

H_data = list(map(int, input().split()))

temp, place = 1000000, -1

ideal_H = (T-A)*1000/6

for i in range(N):
    if abs(ideal_H - H_data[i]) < temp:
        temp = abs(ideal_H - H_data[i])
        place = i + 1
    
print(place)
