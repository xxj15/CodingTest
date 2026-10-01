def solution(land):
    answer = 0
    n = len(land)
    dp = land
    for i in range(1,n):
        for j in range(4):
            new_max = 0
            for k in range(4):
                if k ==j:
                    continue
                new_max = max(dp[i-1][k], new_max)
            dp[i][j]+=new_max
    answer = max(dp[n-1])
    return answer