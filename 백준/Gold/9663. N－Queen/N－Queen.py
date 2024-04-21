import sys

n = int(sys.stdin.readline())
ans = []
cnt = 0

def solve():
    global cnt
    if len(ans) == n:
        cnt += 1

    for i in range(1, n+1):
        p = 0
        if i not in ans:
            for j in range(len(ans)):
                if i == ans[j] - (len(ans)-j) or i == ans[j] + (len(ans)-j):
                    p = 1
                    break

            if p == 0:
                ans.append(i)
                solve()
                ans.pop()

solve()

sys.stdout.write(str(cnt))