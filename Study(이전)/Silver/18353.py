# 병사 배치하기 
N = int(input())
soldiers = list(map(int, input().split()))
# soldiers : 15, 11, 4, 8, 5, 2, 4

dp = [1]*(N)
# dp[0] = 1
# dp[1] = 2
# dp[2] = 2
# dp[3] = 

for i in range(1, N):
  for j in range(0, i): 
    if soldiers[i]< soldiers[j]:
      dp[i]= max(dp[i], dp[j]+ 1)

ans = max(dp)
print(N - ans) # 제거해야하는 개수 구해야하니까 