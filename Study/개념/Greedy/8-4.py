# 바닥 공사 - 타일링 문제 
import sys 
input = sys.stdin.readline

N = int(input())

dp = [0] * 1001 

dp[1] = 1
dp[2] = 3

for i in range(3, N+1):
  dp[i] = (dp[i-1] + dp [i-2] * 2 ) % 796796 # 반복문이니까 bottom up 


print(dp[N])