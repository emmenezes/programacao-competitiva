n_raw = input()
n = int(n_raw)
size = len(n_raw)

f_sum = 0
f_min = 1
f_max = 9
f_min_final = 9 
while (size > 1):
    f_sum += ((f_min + f_max)*(f_max-f_min+1))//2
    f_sum %= 998244353
    f_max *= 10
    f_min_final = f_min_final*10 + 9
    size -= 1

f_min_final = (f_min_final - 9)//10
size = len(n_raw)
f_sum += ((f_min + n-f_min_final)*(n-f_min_final-f_min+1))//2
f_sum %= 998244353

print(f_sum)
