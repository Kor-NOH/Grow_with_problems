import sys

A_input = list(map(str, sys.stdin.readline().strip()))
B_input = list(map(str, sys.stdin.readline().strip()))

dp = [[0] * (len(A_input) + 1) for _ in range(len(B_input) + 1)]

for i in range(1, len(B_input) + 1):
    for j in range(1, len(A_input) + 1):
        if A_input[j - 1] == B_input[i - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

sys.stdout.write(str(max(max(dp))))