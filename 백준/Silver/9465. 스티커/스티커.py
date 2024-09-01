import sys

test_cnt = int(sys.stdin.readline().strip())

for _ in range(test_cnt):
    sticker_map_size = int(sys.stdin.readline().strip())
    sticker_map = [[] for _ in range(2)]
    dp = [[0 for _ in range(sticker_map_size+1)] for _ in range(2)]

    for i in range(2):
        sticker = map(int, sys.stdin.readline().split())
        for s in sticker:
            sticker_map[i].append(s)

    dp[0][0], dp[1][0] = sticker_map[0][0], sticker_map[1][0]

    for i in range(1, sticker_map_size):
        for j in range(2):
            if j == 0:
                dp[j][i] = sticker_map[j][i]+max(dp[j+1][i-1], dp[j+1][i-2])
            else:
                dp[j][i] = sticker_map[j][i]+max(dp[j-1][i-1], dp[j-1][i-2])

    sys.stdout.write(str(max(dp[0][-2], dp[1][-2]))+'\n')