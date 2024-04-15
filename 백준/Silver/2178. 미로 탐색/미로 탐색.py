import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [[] * n for i in range(n)]
for i in range(n):
    coordinate = sys.stdin.readline().strip()
    for j in coordinate:
        graph[i].append(j)

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = deque([(0, 0)])

while queue:
    x, y = queue.popleft()

    for i in range(4):
        next_x, next_y = x+dx[i], y+dy[i]
        if 0 <= next_x < m and 0 <= next_y < n:
            if graph[next_y][next_x] == '1':
                graph[next_y][next_x] = int(graph[y][x]) + 1
                queue.append((next_x, next_y))

print(graph[-1][-1])