import sys

rope_cnt = int(sys.stdin.readline())
rope_list = []
result_list = []

for _ in range(rope_cnt):
    rope_list.append(int(sys.stdin.readline()))

rope_list.sort()

for rope in rope_list:
    result_list.append(rope * rope_cnt)
    rope_cnt -= 1

sys.stdout.write(str(max(result_list)))