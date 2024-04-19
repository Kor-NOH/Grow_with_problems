import sys
import heapq

def rupee(num, cnt):
    INF = int(1e9)
    map_list = [list(map(int, sys.stdin.readline().split())) for i in range(num)]
    dp = [[INF] * num for i in range(num)]
    dp[0][0] = map_list[0][0]
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = [(0, 0)]

    while queue:
        x, y = heapq.heappop(queue)
        for i in range(4):
            next_x, next_y = x+dx[i], y+dy[i]
            if 0 <= next_x < num and 0 <= next_y < num:
                if map_list[next_y][next_x] + dp[y][x] < dp[next_y][next_x]:
                    heapq.heappush(queue, (next_x, next_y))
                    dp[next_y][next_x] = min(map_list[next_y][next_x] + dp[y][x], dp[next_y][next_x])

    sys.stdout.write('Problem '+str(cnt)+': '+str(dp[-1][-1])+'\n')

def input_num():
    global cnt
    cnt += 1
    list_size = int(sys.stdin.readline())
    if list_size != 0:
        rupee(list_size, cnt)
        input_num()

cnt = 0
input_num()