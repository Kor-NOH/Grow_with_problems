import sys

input_num = int(sys.stdin.readline())


if input_num == 1:
    sys.stdout.write('0')
elif input_num == 2 or input_num == 3:
    sys.stdout.write('1')
else:
    dp = [1] * (input_num+1)
    dp[0] = int(1e9)
    for i in range(4, input_num+1):
        # 3과 2로 나누어 떨어지면 1, 아니면 0
        three_div, two_div = 0, 0
        if i % 3 == 0:
            three_div = i // 3

        if i % 2 == 0:
            two_div = i // 2

        dp[i] = min(dp[i-1]+1, dp[three_div]+1, dp[two_div]+1)
    sys.stdout.write(str(dp[input_num]))
