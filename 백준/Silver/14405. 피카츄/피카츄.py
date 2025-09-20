# 피카츄
S = input()
idx = 0 

while idx<len(S):
  if S[idx:idx+2] == 'pi' or S[idx:idx+2] == 'ka':
    idx = idx+2
  elif S[idx:idx+3] == 'chu':
    idx = idx+3 
  else: 
    print('NO')
    break

else: # while 문 돌고 else 블록 실행됨 
    print("YES")
