import sys
import heapq

hole_cnt, tape_len = map(int, sys.stdin.readline().split())
hole_loc = list(map(int, sys.stdin.readline().split()))

heapq.heapify(hole_loc)
safe_dis = 0
tape_cnt = 0

while hole_loc:
    a = heapq.heappop(hole_loc)
    if a > safe_dis:
        tape_cnt += 1
        safe_dis = a + tape_len - 0.5

sys.stdout.write(str(tape_cnt))