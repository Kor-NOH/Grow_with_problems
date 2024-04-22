import sys
from collections import deque

test_cnt = int(sys.stdin.readline())

for i in range(test_cnt):
    n, m = map(int, sys.stdin.readline().split())
    book_list = [0] * (n + 1)
    book_require = [list(map(int, sys.stdin.readline().split())) for j in range(m)]
    book_require.sort(key = lambda x: x[1])
    cnt = 0

    book_require = deque(book_require)

    while book_require:
        a, b = book_require.popleft()
        for j in range(a, b+1):
            if book_list[j] == 0:
                book_list[j] = 1
                cnt += 1
                break

    sys.stdout.write(str(cnt)+'\n')