n = int(input())

words =  []
counter = []

for i in range(n):
    word = input()
    try:
        index = words.index(word)
        print(f"{word}{counter[index]}")
        counter[index] += 1
    except:
        words.append(word)
        counter.append(1)
        print("OK")
    