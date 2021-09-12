'''
Referências:
* https://codeforces.com/blog/entry/213


'''

entrada = input()

seq_max = seq_atual = num_seq = pilha = 0

for parentese in entrada:
    # print(seq_max, seq_atual, num_seq, pilha)
    if parentese == "(":
        pilha += 1
    elif pilha > 0:
        pilha -= 1
        seq_atual += 2
    elif pilha <= 0:
        if seq_atual > seq_max:
            seq_max = seq_atual
            num_seq = 1
        elif seq_atual == seq_max and seq_atual > 0:
            num_seq += 1
        seq_atual = 0

if seq_atual > seq_max:
    seq_max = seq_atual
    num_seq = 1
elif seq_atual == seq_max:
    num_seq += 1

if num_seq == 0:
    print(0, 1)
else:
    print(seq_max, num_seq)