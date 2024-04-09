import sys

n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.insert(0, 0)
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], p[j]+dp[i-j])

sys.stdout.write(str(dp[-1]))