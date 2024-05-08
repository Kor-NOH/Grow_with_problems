# 총 F층, 스타트링 현재 위치 S, 위치 G,  U업, D다운
import sys
from collections import deque

f, s, g, u, d = map(int, sys.stdin.readline().split())
result = -1

check = [0 for _ in range(f+1)]
check[s] = 1

queue = deque()
queue.append(s)

while queue:
    p = queue.popleft()

    if p == g:
        result = check[p]-1
        break

    else:
        for new_p in (p+u, p-d):
            if 0 < new_p <= f and check[new_p] == 0:
                check[new_p] = check[p]+1
                queue.append(new_p)

if result == -1:
    sys.stdout.write('use the stairs')
else:
    sys.stdout.write(str(result))