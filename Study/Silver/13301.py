#타일 장식물 
import sys
input = sys.stdin.readline

N = int(input()) # 타일 개수 입력받음 

dp = [0]*(N+1)

dp[0]=0
dp[1]=4
dp[2]=6

for i in range(3,N+1):
  dp[i]= dp[i-1]+dp[i-2]

print(dp[N])