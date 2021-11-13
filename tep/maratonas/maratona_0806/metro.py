n, s = map(int, input().split())
n, s = n - 1, s - 1
metro_ida = list(map(int, input().split()))
metro_volta = list(map(int, input().split()))

if (metro_ida[0] == 0 or (metro_ida[s] == 0 and metro_volta[s] == 0)):
    print("NO")
elif(metro_ida[s] == 1):
    print("YES")
else:
    resposta = "NO"
    for i in range(s,n + 1):
        if (metro_ida[i] and metro_volta[i]):
            resposta = "YES"
            break
    print(resposta)
