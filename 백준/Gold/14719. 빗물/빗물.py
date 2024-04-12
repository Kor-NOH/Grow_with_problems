import sys

h, w = map(int, sys.stdin.readline().split())
block_list = list(map(int, sys.stdin.readline().split()))

result = 0

for i in range(1, w-1):
    left_block = max(block_list[:i])
    right_block = max(block_list[i+1:])

    sec_high_block = min(left_block, right_block)

    if block_list[i] < sec_high_block:
        result += sec_high_block - block_list[i]

sys.stdout.write(str(result))