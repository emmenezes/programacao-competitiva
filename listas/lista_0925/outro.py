for s in[*open(0)][1:]:
 for i in range(n:=int(s)):print('()'*i+'('+'()'*(n-i-1)+')')