import sys

input_num = map(int, sys.stdin.readline().strip())
num_list = list(input_num)
g_n = num_list[0]
d_c = 0

if len(num_list) > 1:
    for i in range(1, len(num_list)):
        if num_list[i] != g_n:
            d_c += 1
            g_n = num_list[i]

    sys.stdout.write(str((d_c+1)//2))
else:
    sys.stdout.write('0')