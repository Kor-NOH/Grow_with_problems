import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())
tomato_list = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

queue = deque([])
dx = [0 , 0 , 1 , -1]
dy = [1, -1, 0, 0]
result = 1

for i in range(n):
    for j in range(m):
        if tomato_list[i][j] == 1:
            queue.append((i, j))

while queue:
    y, x = queue.popleft()
    for i in range(4):
        next_y = y + dy[i]
        next_x = x + dx[i]
        if 0 <= next_y < n and 0 <= next_x < m and tomato_list[next_y][next_x] == 0:
            tomato_list[next_y][next_x] = tomato_list[y][x] + 1
            queue.append((next_y, next_x))

for i in range(n):
    for j in range(m):
        if tomato_list[i][j] == 0:
            result = 0

if result == 0:
    sys.stdout.write('-1')
else:
    max_num = 0
    for i in tomato_list:
        for j in i:
            if j > max_num:
                max_num = j

    sys.stdout.write(str(max_num-1))