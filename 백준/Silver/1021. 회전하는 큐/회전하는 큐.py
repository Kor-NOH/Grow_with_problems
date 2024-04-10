import sys
from collections import deque

def left(num):
    for i in range(num):
        num_list.appendleft(num_list.pop())

def right(num):
    for i in range(num):
        num_list.append(num_list.popleft())


n, m = map(int, sys.stdin.readline().split())
num_list = deque([i for i in range(1, n+1)])
goal_list = deque(map(int, sys.stdin.readline().split()))
result = 0

for goal_num in goal_list:
    for i in range(len(num_list)):
        if num_list[i] == goal_num:
            if i < len(num_list) - i:
                right(i)
                result += i
                num_list.popleft()
                break

            else:
                left(len(num_list)-i)
                result += len(num_list)-i
                num_list.popleft()
                break

sys.stdout.write(str(result))