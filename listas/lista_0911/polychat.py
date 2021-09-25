# Incompleta! Depende de N ainda!

n = int(input())

people = 0
data = 0

for i in range(n):
    entry = input()
    if entry[0] == "+":
        people += 1
    elif entry[0] == "-":
        people -= 1
    else:
        text = entry.split(":")
        tam = len(text[1])
        data += tam*people
    
print(data)

'''
COMO USAR EOF EM Python

traffic = 0
total_grupo = 0
while (True):
  try:
    linha = input().strip()
    if linha[0] == '+':
      total_grupo += 1
    elif linha[0] == '-':
      total_grupo -= 1
    else:
      comando, message =linha.split(':')
      tamanho = len(message)
      traffic += (total_grupo*tamanho)
 
  except EOFError:
    print(traffic)
    break
  	     
'''