import sys

box_cnt = int(sys.stdin.readline())
box_list = list(map(int, sys.stdin.readline().split()))
result_list = [1]*box_cnt

for i in range(1, box_cnt):
    for j in range(i+1):
        if box_list[i] > box_list[j]:
            result_list[i] = max(result_list[i], result_list[j]+1)

sys.stdout.write(str(max(result_list)))