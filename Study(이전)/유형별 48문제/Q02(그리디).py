# 곱하기 혹은 더하기

number = list(map(int, input()))
ans = number[0]

for i in  range(1, len(number)): 
  if ans + number[i] >= ans*number[i]:
    ans =  ans + number[i] 

  else : 
    ans = ans*number[i]

print(ans)