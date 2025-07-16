# 효율적인 화폐 구성 
# 그리디에서 다른 거스름돈 문제와의 차이 : 화폐 단위에서 큰 단위가 작은 단위의 배수가 아니다 

import sys 
input = sys.stdin.readline

N, M = map(int, input().split())

money = [int(input()) for _ in range(N)]

dp = [10001] * (M+1)

dp[0] = 0

for i in range(N):
  for j in range(money[i], M+1):
    # (i-k) 원을 만드는 방법이 존재
    if dp[j - money[i]] != 10001 : 
      dp[j] = min(dp[j], dp[j - money[i]]+1)

if dp[M] != 10001:
  print(dp[M])

else:
  print(-1)