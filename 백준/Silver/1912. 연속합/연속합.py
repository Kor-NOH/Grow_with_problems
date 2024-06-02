import sys

cnt = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

for i in range(1, cnt):
    num_list[i] = max(num_list[i]+num_list[i-1], num_list[i])

# sys.stdout.write(str(num_list) + '\n')
sys.stdout.write(str(max(num_list)))