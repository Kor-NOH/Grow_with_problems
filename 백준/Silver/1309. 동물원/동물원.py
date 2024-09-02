import sys

z_size = int(sys.stdin.readline().strip())
dp = [[] for _ in range(z_size)]
dp[0] = [1, 1, 1]
for i in range(1, z_size):
    dp[i] = [sum(dp[i-1])%9901,(dp[i-1][0]+dp[i-1][2])%9901,(dp[i-1][0]+dp[i-1][1])%9901]

sys.stdout.write(str(sum(dp[-1])%9901))