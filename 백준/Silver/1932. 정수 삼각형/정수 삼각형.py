import sys

layer = int(sys.stdin.readline())
int_triangle = [0] * layer

for i in range(layer):
    int_triangle[i] = list(map(int, sys.stdin.readline().split()))

dp = [[0]*(i+1) for i in range(layer)]
dp[0][0] = int_triangle[0][0]

for i in range(1, layer):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + int_triangle[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + int_triangle[i][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + int_triangle[i][j]

sys.stdout.write(str(max(dp[layer-1])))
