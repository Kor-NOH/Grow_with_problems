import sys

m, n, h = map(int, sys.stdin.readline().split())
t_list, q_1, q_2 = [], [], []
day = 0

for i in range(h):
    t = []
    for j in range(n):
        t.append(list(map(int, sys.stdin.readline().split())))
    t_list.append(t)

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for i in range(h):
    for j in range(n):
        for k in range(m):
            if t_list[i][j][k] == 1:
                q_1.append([i, j, k])

while q_1:
    day += 1
    q_2 = q_1[:]
    q_1.clear()
    while q_2:
        z, y, x = q_2.pop()
        for i in range(6):
            next_z, next_y, next_x = z + dz[i], y + dy[i], x + dx[i]
            if 0 <= next_z < h and 0 <= next_y < n and 0 <= next_x < m:
                if t_list[next_z][next_y][next_x] == 0:
                    t_list[next_z][next_y][next_x] = 1
                    q_1.append([next_z, next_y, next_x])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if t_list[i][j][k] == 0:
                print('-1')
                exit()

print(day-1)