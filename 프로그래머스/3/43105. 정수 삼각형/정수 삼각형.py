def solution(triangle):
    dp = [[0] * len(n) for n in triangle]
    dp[0][0] = triangle[0][0]
    
        
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                dp[i][0] = dp[i-1][0] + triangle[i][0]
            elif j == len(triangle[i]) - 1:
                dp[i][-1] = dp[i-1][-1] + triangle[i][-1]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]
                
    answer = max(dp[-1])
    return answer