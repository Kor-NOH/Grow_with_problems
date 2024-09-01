import sys
from collections import deque

test_cnt = int(sys.stdin.readline().strip())

for _ in range(test_cnt):
    m, n, k = map(int, sys.stdin.readline().split())
    v_m = [[0] * m for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    cnt = 0

    queue = deque()

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        v_m[y][x] = 1

    for i in range(n):
        for j in range(m):
            if v_m[i][j] == 1:
                cnt += 1
                queue.append((i,j))
                while queue:
                    y, x = queue.pop()

                    v_m[y][x] = 0
                    for k in range(4):
                        next_x, next_y = x+dx[k], y+dy[k]
                        if 0 <= next_x < m and 0 <= next_y < n:
                            if v_m[next_y][next_x] == 1 :
                                queue.append((next_y, next_x))

    print(cnt)