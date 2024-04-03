import sys

n = int(sys.stdin.readline())

schedule_list = []
dp = [0] * (n+1)

for _ in range(n):
    t, p = map(int, sys.stdin.readline().split())
    schedule_list.append([t, p])

for i in range(n+1):
    max_num = 0
    for j in range(0, i):
        if schedule_list[j][0] <= n-j and schedule_list[j][0] + j <= i and schedule_list[j][1] + dp[j] > max_num:
            max_num = schedule_list[j][1]+dp[j]

    dp[i] = max_num

sys.stdout.write(str(max(dp)))