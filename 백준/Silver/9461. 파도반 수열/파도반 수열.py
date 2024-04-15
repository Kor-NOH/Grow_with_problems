import sys

test_cnt = int(sys.stdin.readline())

for i in range(test_cnt):
    n = int(sys.stdin.readline())
    num_list = [0, 1, 1, 1, 2]

    if n > 4:
        add_cnt = n - 4
        for j in range(add_cnt):
            add_num = num_list[-1] + num_list[-5]
            num_list.append(add_num)

    sys.stdout.write(str(num_list[n])+'\n')