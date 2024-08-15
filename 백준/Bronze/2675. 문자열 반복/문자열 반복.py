import sys

test_cnt = int(sys.stdin.readline())

for _ in range(test_cnt):

    l_cnt, input_s = sys.stdin.readline().split()
    s_list = list(input_s)

    for i in range(len(s_list)):
        sys.stdout.write(str(s_list[i]) * int(l_cnt))
    sys.stdout.write('\n')