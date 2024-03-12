import sys

h_num = int(sys.stdin.readline())
h_list = list(map(int, sys.stdin.readline().split()))
result_list = [0]*h_num

for i in range(h_num):
    for j in range(len(result_list)):
        if h_list[i] == 0 and result_list[j] == 0:
            result_list[j] = i+1
            break
        elif h_list[i] != 0 and result_list[j] == 0:
            h_list[i] -= 1

sys.stdout.write(' '.join(map(str, result_list)))