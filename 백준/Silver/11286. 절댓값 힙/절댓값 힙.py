import sys
import heapq

cnt = int(sys.stdin.readline())
num_list = []

for _ in range(cnt):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(num_list) == 0:
            sys.stdout.write('0\n')
        else:
            sys.stdout.write(str(heapq.heappop(num_list)[1])+'\n')

    else:
        heapq.heappush(num_list, (abs(num), num))