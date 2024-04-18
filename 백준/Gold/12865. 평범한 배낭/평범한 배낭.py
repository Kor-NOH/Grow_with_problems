import sys

things_cnt, backpack = map(int, sys.stdin.readline().split())
things_list = [list(map(int, sys.stdin.readline().split())) for _ in range(things_cnt)]
dp = [[0] * (backpack+1) for _ in range(things_cnt+1)]

for i in range(things_cnt):
    for j in range(backpack+1):
        if j >= things_list[i][0]:
            dp[i+1][j] = max(things_list[i][1]+dp[i][j-things_list[i][0]], dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]

if things_cnt == 0:
    sys.stdout.write('0')
else:
    sys.stdout.write(str(dp[-1][-1]))