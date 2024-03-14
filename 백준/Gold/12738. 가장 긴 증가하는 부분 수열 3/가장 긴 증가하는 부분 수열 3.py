import sys
from bisect import bisect_left

cnt = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

lis = [n_list[0]]

for num in n_list[1:]:
    if num > lis[-1]:
        lis.append(num)
    else:
        lis[bisect_left(lis, num)] = num

sys.stdout.write(str(len(lis)))