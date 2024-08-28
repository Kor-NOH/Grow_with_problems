import sys
import heapq

num_cnt = int(sys.stdin.readline())
num_list = []
result = 0
for _ in range(num_cnt):
    num_list.append(int(sys.stdin.readline()))
heapq.heapify(num_list)

while len(num_list)>=2:
    a = heapq.heappop(num_list)
    b = heapq.heappop(num_list)
    result += a+b
    num_list.append(a+b)

sys.stdout.write(str(result))