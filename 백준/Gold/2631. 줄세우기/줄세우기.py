import sys

n_list = []
cnt = int(sys.stdin.readline())
for _ in range(cnt):
    n = int(sys.stdin.readline())
    n_list.append(n)

dp = [1] * cnt

for i in range(1, cnt):
    for j in range(i):
        if n_list[i] > n_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

sys.stdout.write(str(cnt - max(dp)))