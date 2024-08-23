import sys

input_n = int(sys.stdin.readline())

if input_n == 1:
    sys.stdout.write('1/1')
else:
    sum_n, new_n = 1, 1
    past_n = 1
    while new_n < input_n:
        sum_n += 1
        past_n = new_n
        new_n += sum_n

    down_n = sum_n - (input_n - (past_n + 1))
    up_n = 1 + (input_n - (past_n + 1))

    if sum_n % 2 == 1:
        sys.stdout.write(str(down_n)+'/'+str(up_n))
    else:
        sys.stdout.write(str(up_n) + '/' + str(down_n))