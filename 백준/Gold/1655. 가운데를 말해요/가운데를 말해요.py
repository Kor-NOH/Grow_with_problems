import sys
import heapq

cnt = int(sys.stdin.readline())

left_list, right_list, answer_list = [], [], []

for _ in range(cnt):
    num = int(sys.stdin.readline())
    if len(left_list) == len(right_list):
        heapq.heappush(left_list, [-num, num])
    else:
        heapq.heappush(right_list, [num, num])

    if right_list and left_list[0][1] > right_list[0][1]:
        a = heapq.heappop(left_list)[1]
        b = heapq.heappop(right_list)[1]
        heapq.heappush(right_list, [a, a])
        heapq.heappush(left_list, [-b, b])

    answer_list.append(left_list[0][1])

sys.stdout.write('\n'.join(map(str, answer_list)))