import sys
input_num = int(sys.stdin.readline())
dp = [0] * (input_num +1)
dp[1] = 1

if input_num == 0:
    sys.stdout.write('0')

elif input_num == 1:
    sys.stdout.write('1')

else:
    for i in range(2, input_num+1):
        dp[i] = dp[i-1] + dp[i-2]

    sys.stdout.write(str(dp[input_num]))