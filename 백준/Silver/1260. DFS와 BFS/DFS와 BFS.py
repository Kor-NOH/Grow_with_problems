import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
num_list = [[0]*(n+1) for i in range(n+1)]

dfs_check_list, bfs_check_list = [0]*(n+1), [0]*(n+1)
dfs_result_list,bfs_result_list = [], []

deque = deque()

def dfs(num):
    dfs_check_list[num] = 1
    dfs_result_list.append(num)
    for i in range(n+1):
        if dfs_check_list[i] == 0 and num_list[num][i] == 1:
            dfs(i)

def bfs(num):
    deque.append(num)
    bfs_check_list[num] = 1
    while deque:
        num = deque.popleft()
        bfs_result_list.append(num)
        for i in range(1, n+1):
            if bfs_check_list[i] == 0 and num_list[num][i] == 1:
                deque.append(i)
                bfs_check_list[i] = 1



for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    num_list[a][b] = 1
    num_list[b][a] = 1

dfs(v)
print(*dfs_result_list)

bfs(v)
print(*bfs_result_list)