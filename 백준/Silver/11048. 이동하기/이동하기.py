import sys
n, m = map(int, sys.stdin.readline().split())
candy_list = [0] * n

result = [[0] * m for _ in range(n)]

for i in range(n):
    candy_list[i] = list(map(int, sys.stdin.readline().split()))

result[0][0] = candy_list[0][0]

for i in range(1, m):
    result[0][i] = result[0][i-1] + candy_list[0][i]

for i in range(1, n):
    result[i][0] = result[i-1][0] + candy_list[i][0]

for i in range(1, n):
    for j in range(1, m):
        result[i][j] = max(result[i-1][j-1], result[i-1][j], result[i][j-1]) + candy_list[i][j]

sys.stdout.write(str(result[n-1][m-1]))