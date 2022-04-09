t = int(input())

for _ in range(t):
    s = input()
    c = input()

    if c not in s:
        print("No")
    else:
        list_id = [i for i, v in enumerate(s) if v == c]
        list_id_2 = [i for i in list_id if i%2 == 0]
        
        if list_id_2:
            print('Yes')
        else:
            print('No')