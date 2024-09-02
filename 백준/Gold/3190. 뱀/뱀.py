import sys
from collections import deque

map_size = int(sys.stdin.readline().strip())
m = [[0 for _ in range(map_size)]for _ in range(map_size)]

tick = 0

apple_cnt = int(sys.stdin.readline().strip())
for i in range(apple_cnt):
    x, y = map(int, sys.stdin.readline().split())
    m[x-1][y-1] = 2

snake_turn_cnt = int(sys.stdin.readline().strip())
snake_turn = list(sys.stdin.readline().split() for i in range(snake_turn_cnt))

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction = 0

queue = deque([(0,0)])

while True:

    tick += 1

    x, y = queue[-1]
    next_x = x+dx[direction]
    next_y = y+dy[direction]

    if next_x < 0 or next_x >= map_size or next_y < 0 or next_y >= map_size or (next_x, next_y) in queue:
        break
    else:
        queue.append((next_x, next_y))
        if m[next_y][next_x] != 2:
            queue.popleft()
        else:
            m[next_y][next_x] = 0

    for i in range(len(snake_turn)):
        if int(snake_turn[i][0]) == tick:
            if snake_turn[i][1] == 'L':
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4

print(tick)