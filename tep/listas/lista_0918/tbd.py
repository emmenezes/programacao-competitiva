date = list(map(int, input().split('/')))

if date[0] < 2019 or (date[0] == 2019 and date[1] < 4) or (date[0] == 2019 and date[1] == 4 and date[2] <= 30):
    print("Heisei")
else:
    print("TBD")