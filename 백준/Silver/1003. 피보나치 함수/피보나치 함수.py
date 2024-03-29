import sys

test_cnt = int(sys.stdin.readline())

for _ in range(test_cnt):
    input_num = int(sys.stdin.readline())

    if input_num == 0:
        sys.stdout.write('1 0\n')
    elif input_num == 1:
        sys.stdout.write('0 1\n')
    else:
        dp = [[0, 0] for _ in range(input_num+1)]
        dp[0] = [1, 0]
        dp[1] = [0, 1]

        for i in range(2, input_num+1):
            dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
            dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

        sys.stdout.write(str(dp[input_num][0])+ ' ' + str(dp[input_num][1]) + '\n')