# 1,2,3 더하기
# 조건: N은 11 이하 자연수 

T = int(input())

dp = [0] * 12
dp[1] = 1 # 1
dp[2] = 2 # 2 = 1+1
dp[3] = 4 # 3 = 2+1 = 1+2 = 1+1+1 
# 4를 만드는 법 = 3(dp[3]) + 1 = 2(dp[2])+2 = 1(dp[1]) + 3 

for i in range(4, 12):
  dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

for _ in range(T):
  N = int(input())
  print(dp[N])


