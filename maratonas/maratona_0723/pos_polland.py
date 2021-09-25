n = int(input())

if (n > 2):
    if (n%2 != 0):
        print(1)
    else:
        print(n-2)
else:
    if (n == 1):
        print(3)
    else:
        print(4)

# Aprendizados:
# O principal erro foi ignorar os casos triviais de 1 e 2 
# Também aprendi uma fórmula lustrosa que poderia ter simplicado minha vida, 
# e assim não precisaria trabalhar ou com par ou com ímpar