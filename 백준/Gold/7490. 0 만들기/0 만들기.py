import sys

def dfs(n, idx, rst):
    if idx == n:
        ans = eval(rst.replace(' ', ''))
        if ans == 0:
            result_list.append(rst)
        return
    else:
        n_idx = idx + 1
        # 공백
        dfs(n, n_idx, rst + ' ' + str(n_idx))
        # +
        dfs(n, n_idx, rst + '+' + str(n_idx))
        # -
        dfs(n, n_idx, rst + '-' + str(n_idx))

cnt = int(sys.stdin.readline())
for _ in range(cnt):
    num = int(sys.stdin.readline())
    result_list = []
    dfs(num, 1, '1')

    for a in result_list:
        print(a)
    print()