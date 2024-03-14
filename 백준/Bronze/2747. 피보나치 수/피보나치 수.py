import sys

num = int(sys.stdin.readline())
dp = [0] * (num + 1)
dp[1] = 1

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if dp[x] != 0:
        return dp[x]

    dp[x] = fibo(x-1) + fibo(x-2)
    return dp[x]

sys.stdout.write(str(fibo(num)))