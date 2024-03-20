import sys

a, b = map(int, sys.stdin.readline().split())

name_list, result_list = set(), []
for _ in range(a):
    not_listen = sys.stdin.readline().strip()
    name_list.add(not_listen)

for _ in range(b):
    not_see = sys.stdin.readline().strip()
    if not_see in name_list:
        result_list.append(not_see)

result_list.sort()
sys.stdout.write(str(len(result_list))+'\n')
sys.stdout.write('\n'.join(result_list))