N, T = map(int, input().split())
lista = []

for i in range(N):
    t, d = map(int, input().split())
    lista.append([t, d])

lista_tempo = sorted(lista, key=lambda x:x[0])
lista_desconto = sorted(lista, key=lambda x:-x[1])

cursos_1=0
descontos_1 = 0
res_1 = []
tempo = T

for i in range(N):
    if lista_tempo[i][1] <= tempo:
        tempo -= lista_tempo[i][1]
        descontos_1 

tempo = T
cursos_2=0
descontos_2 = 0
res_2 = []