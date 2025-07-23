# 문자열 뒤집기

number = list(map(int, input()))

cnt0 = 0 
cnt1 = 0

if number[0] == 1 : 
  cnt0 += 1

else : 
  cnt1 += 1

for i in range(len(number)-1):
  if number[i]!=number[i+1]:
    if number[i+1]==1: 
      cnt0 += 1
    else :
      cnt1 += 1

print(min(cnt0, cnt1))