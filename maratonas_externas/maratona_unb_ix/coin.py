t = int(input())

for _ in range(t):
    n, s = map(int, input().split())
    bin = int(input(), 2)
    if bin%n == 0:
        print("To the moon!")
    else:
        print("Phishing de criptomoeda.")