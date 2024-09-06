import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
s_n, s_m, s_d = map(int, sys.stdin.readline().split())
clean_cnt = 0
loc = []

if s_d == 0:
    direction = 1
elif s_d == 1:
    direction = 0
elif s_d == 2:
    direction = 3
else:
    direction = 2

for i in range(n):
    loc_con = list(map(int, sys.stdin.readline().split()))
    loc.append(loc_con)

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

queue = deque([(s_n, s_m)])

while queue:
    a, b = queue.pop()
    dirt_area_find = 0

    if loc[a][b] == 0:
        clean_cnt += 1
        loc[a][b] = 2

    for i in range(4):
        direction = (direction + 1) % 4
        next_a, next_b = a + dy[direction], b + dx[direction]
        if 0 <= next_a < n and 0 <= next_b < m:
            if loc[next_a][next_b] == 0:
                queue.append((next_a, next_b))
                dirt_area_find = 1
                break

    if dirt_area_find == 0:
        next_a, next_b = a + dy[(direction - 2) % 4], b + dx[(direction - 2) % 4]
        if 0 <= next_a < n and 0 <= next_b < m and loc[next_a][next_b] != 1:
            queue.append((next_a, next_b))

        else:
            break

sys.stdout.write(str(clean_cnt))