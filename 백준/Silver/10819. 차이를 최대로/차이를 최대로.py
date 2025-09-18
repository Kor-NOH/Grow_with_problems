import sys
from itertools import permutations

n = int(sys.stdin.readline())
result = 0
num_list = list(map(int, sys.stdin.readline().split()))
per = list(permutations(num_list, n))

for i in per:
    sum = 0
    for j in range(n-1):
        sum += abs(i[j] - i[j+1])

    result = max(result, sum)

print(result)