# 럭키 스트레이트 
N = list(map(int, input()))
half = len(N) // 2
total = sum(N)

first_half = 0 

for i in range(half):
  first_half += N[i]

if first_half == total - first_half: 
  print("LUCKY")

else: 
  print("READY")
