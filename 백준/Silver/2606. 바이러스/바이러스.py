import sys

def dfs(num):
    com_status[num] = 1
    for i in range(com_cnt+1):
        if com_status[i] == 0 and com_con_list[num][i] == 1:
            dfs(i)

com_cnt = int(sys.stdin.readline())
connect_cnt = int(sys.stdin.readline())
com_con_list = [[0]*(com_cnt+1) for _ in range(com_cnt+1)]

com_status = [0] * (com_cnt+1)
#0 양호, 1 감염

result = 0

for _ in range(connect_cnt):
    a, b = map(int, sys.stdin.readline().split())
    com_con_list[a][b] = 1
    com_con_list[b][a] = 1

dfs(1)

for i in range(len(com_status)):
    if com_status[i] == 1:
        result += 1

sys.stdout.write(str(result-1))