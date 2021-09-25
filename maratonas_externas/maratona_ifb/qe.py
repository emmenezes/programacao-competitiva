def desromano(num):
    eqv = 0
    ant = "Z"
    pos = -1
    while abs(pos) != len(num)+1:
        atual = num[pos]
        if atual == "I" and (ant == "V" or ant == "X"):
            eqv += -1
        elif atual == "X" and (ant == "L" or ant == "C"):
            eqv += -10
        elif atual == "C" and (ant == "D" or ant == "M"):
            eqv += -100
        elif atual == "I":
            eqv += 1
        elif atual == "V":
            eqv += 5
        elif atual == "X":
            eqv += 10
        elif atual == "L":
            eqv += 50
        elif atual == "C":
            eqv += 100
        elif atual == "D":
            eqv += 500
        elif atual == "M":
            eqv += 1000
        ant = atual
        pos -= 1

    return eqv

def romano(num):
    eqv = ""

    while num != 0:
        if num >= 1000:
            num -= 1000
            eqv += "M"
        elif num >= 900:
            num -= 900
            eqv += "CM"
        elif num >= 500:
            num -= 500
            eqv += "D"
        elif num >= 400:
            num -= 400
            eqv += "CD"
        elif num >= 100:
            num -= 100
            eqv += "C"
        elif num >= 90:
            num -= 90
            eqv += "XC"
        elif num >= 50:
            num -= 50
            eqv += "L"
        elif num >= 40:
            num -= 40
            eqv += "XL"
        elif num >= 10:
            num -= 10
            eqv += "X"
        elif num == 9:
            num -= 9
            eqv += "IX"
        elif num >= 5:
            num -= 5
            eqv += "V"
        elif num == 4:
            num -= 4
            eqv += "IV"
        else:
            num -= 1
            eqv += "I"
    
    return eqv

A, B = input().split()
A, B = desromano(A), desromano(B)
print(romano(A+B))
