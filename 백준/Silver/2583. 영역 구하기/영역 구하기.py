import sys
from collections import deque

m, n, k = map(int, sys.stdin.readline().split())
n_list = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            n_list[i][j] = 1

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result_list = []

for i in range(m):
    for j in range(n):
        if n_list[i][j] == 0:
            area = 0
            queue = [(i, j)]
            while queue:
                y, x = queue.pop()

                if n_list[y][x] == 0:
                    n_list[y][x] = 2
                    area += 1

                for k in range(4):
                    next_y, next_x = y + dy[k], x + dx[k]
                    if 0 <= next_y < m and 0 <= next_x < n:
                        if n_list[next_y][next_x] == 0:
                            queue.append((next_y, next_x))

            result_list.append(area)

result_list.sort()
print(len(result_list))
for result in result_list:
    sys.stdout.write(str(result) + ' ')