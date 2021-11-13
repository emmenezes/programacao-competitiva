a = int(input())
setes = 1
seteSeguidos = 7
if(a%2 == 0):
    print(-1)
else:
    while (setes <= a):
        if(seteSeguidos%a == 0):
            break
        else:
            seteSeguidos = (seteSeguidos*10 + 7)%a
            setes += 1
    if (setes > a):
        print(-1)
    else:
        print(setes)

# Aprendizados:
# Sempre tentar reduzir números, às vezes pode não ser intuitivo então é bom escrever um pouco
# Tomar cuidado com os casos limites, e se atentar aos casos enormes. Realmente existem?
