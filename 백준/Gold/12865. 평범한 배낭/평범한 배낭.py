import sys

things_cnt, backpack = map(int, sys.stdin.readline().split())
things_list = [list(map(int, sys.stdin.readline().split())) for _ in range(things_cnt)]
dp = [0] * (backpack + 1)

for w, v in things_list:
    for j in range(backpack, w - 1, -1):
        dp[j] = max(dp[j], dp[j - w] + v)

sys.stdout.write(str(dp[backpack]))
