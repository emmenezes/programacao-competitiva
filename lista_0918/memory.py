def alloc(controle, mem, maxi, tam):
    tem_espaco = False
    onde  = -1
    pos = -1
    if not mem:
        if tam <= maxi:
            mem.append([controle, 1, tam])
            return [controle, mem]
        else:
            return ["NULL"]
    elif len(mem) == 1:
        value = mem[0]
        if value[1] != 1:
            if tam <= value[1] - 1:
                tem_espaco = True
                onde = 1
                pos = 0
        if not tem_espaco:
            if tam <= maxi - value[2]:
                tem_espaco = True
                onde = value[2]+1
                pos = 1
    else:
        for index, value in enumerate(mem):
            if index == 0 and value[1] != 1:
                if tam <= value[1] - 1:
                    tem_espaco = True
                    onde = 1
                    pos = 0
                    break
            if index == len(mem)-1:
                if tam <= maxi - value[2]:
                    tem_espaco = True
                    onde = value[2] + 1
                    pos = -1
                    break
            else:
                disp = mem[index+1][1] - value[2] - 1
                if tam <= disp:
                    tem_espaco = True
                    onde = value[2] + 1
                    pos = index + 1
                    break
    
    if tem_espaco:
        if pos == -1:
            mem.append([controle, onde, onde + tam - 1])
        else:
            mem.insert(pos, [controle, onde, onde + tam - 1])
        return [controle, mem]
    else:
        return ["NULL"]

def erase(mem, index):
    for i in range(len(mem)):
        if mem[i][0] == index:
            del mem[i]
            break
    return mem

def defragment(mem):
    nova_mem = []
    pos = 1
    for espaco in mem:
        tam = espaco[2] - espaco[1]
        nova_mem.append([espaco[0], pos, pos + tam])
        pos += tam + 1
    return nova_mem

n, tam = map(int, input().split())

mem = []
blocos = []
controle = 1

for i in range(n):
    comando = input().split()
    if comando[0] == "alloc":
        res = alloc(controle, mem, tam, int(comando[1]))
        print(res[0])
        if res[0] != "NULL":
            controle += 1
            blocos.append(res[0])
            mem = res[1]
    elif comando[0] == "erase":
        if int(comando[1]) in blocos:
            mem = erase(mem, int(comando[1]))
            blocos.remove(int(comando[1]))
        else:
            print("ILLEGAL_ERASE_ARGUMENT")
    else:
        mem = defragment(mem)
    #print(blocos)
    #print(mem)