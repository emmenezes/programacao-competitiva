# Erros na questão
# - Se eu tivesse escrito a fórmula, não teria errado


soma = 0

s = input()
k = int(input())
w = [0] + list(map(int, input().split()))
l = [0 for _ in range(27)]
n = len(s) + 1

for i in range(len(s)):
    sx = s[i]
    soma += w[ord(sx)-96]*(i+1)

max_w = max(w)

soma += max_w*(2*n + k -1)*k//2

print(soma)


