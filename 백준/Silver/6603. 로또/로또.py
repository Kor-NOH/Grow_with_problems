import sys

def backtracking(num, num_list):
    global ans

    if len(ans) == 6:
        sys.stdout.write(' '.join(map(str, ans))+'\n')
        return

    for i in range(num, len(num_list)):
        if num_list[i] not in ans:
            ans.append(num_list[i])
            backtracking(i, num_list)
            ans.pop()

def input_num():
    num_list = list(map(int, sys.stdin.readline().split()))
    num_list.pop(0)
    sorted_num_list = sorted(num_list)

    global ans
    ans = []
    if len(num_list) != 0:
        backtracking(0, sorted_num_list)
        sys.stdout.write('\n')
        input_num()

ans = []
input_num()