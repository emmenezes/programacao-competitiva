code = input()

for i in range(3):
    if code[i] == code[i+1]:
        print("Bad")
        quit()

print("Good")