S = input()

if (S[0] != "A"):
    print("WA")
    quit()

upper_c = 0

for i in range(2, len(S)-1):
    if (S[i] == "C"):
        upper_c += 1

if (upper_c != 1):
    print("WA")
    quit()

for i in range(1, len(S)-1):
    if (S[i].isupper() and S[i] != "C"):
        print("WA")
        quit()

print("AC")
