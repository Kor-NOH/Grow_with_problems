import sys

cnt = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
dp = [1] * cnt

for i in range(1, cnt):
    for j in range(i):
        if num_list[i] > num_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

sys.stdout.write(str(max(dp)))