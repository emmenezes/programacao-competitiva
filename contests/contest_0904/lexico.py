S = []
S.append(input())
S.append(input())
S.append(input())

contests = ["ABC", "ARC", "AGC", "AHC"]

for Sx in S:
    contests.remove(Sx)

print(*contests)