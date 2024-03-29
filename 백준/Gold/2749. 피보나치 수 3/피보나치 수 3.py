import sys
input_num = int(sys.stdin.readline())
cycle = 1000000 // 10 * 15
dp = [0] * cycle
dp[1] = 1

if input_num == 0:
    sys.stdout.write('0')

elif input_num == 1:
    sys.stdout.write('1')

else:
    for i in range(2, cycle):
        dp[i] = (dp[i-1] + dp[i-2]) % 1000000

    sys.stdout.write(str(dp[input_num%cycle]))