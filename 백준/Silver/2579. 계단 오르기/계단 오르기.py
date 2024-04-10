import sys

cnt = int(sys.stdin.readline())
stair_list = [int(sys.stdin.readline()) for i in range(cnt)]
dp = [0] * (cnt+1)

if cnt == 1:
    sys.stdout.write(str(stair_list[0]))
elif cnt == 2:
    sys.stdout.write(str(sum(stair_list)))
else:
    dp[1], dp[2] = stair_list[0], stair_list[0] + stair_list[1]
    stair_list.insert(0, 0)
    for i in range(3, cnt+1):
        dp[i] = max(dp[i-3] + stair_list[i-1], dp[i-2]) + stair_list[i]

    sys.stdout.write(str(dp[-1]))