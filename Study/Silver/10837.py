# 동전 게임 
import math 

K = int(input())
C = int(input())

def check (y, d, K ): 
  if M == N : 
    return 1
  elif M > N : # 영희가 이김 
    return 1 if diff <= remain_game + 2 else 0 
  else : 
    return 1 if diff <= remain_game + 1 else 0 
  

for _ in range(C):
  M, N = map(int, input().split())
  diff = abs(M - N) # 점수차 
  remain_game = K - max(M, N) # 남은 게임 수 

  print(check(M, N, K))


