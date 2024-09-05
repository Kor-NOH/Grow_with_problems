import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
j_list = []
b_list = []
result = 0

for i in range(n):
    j_list.append(list(map(int, sys.stdin.readline().split())))

for i in range(k):
    b_list.append(int(sys.stdin.readline().strip()))

j_list.sort(); b_list.sort()
tmp = []

for bag in b_list:
    while j_list and j_list[0][0] <= bag:
        heapq.heappush(tmp, -j_list[0][1])
        heapq.heappop(j_list)

    if tmp:
        result -= heapq.heappop(tmp)

print(result)