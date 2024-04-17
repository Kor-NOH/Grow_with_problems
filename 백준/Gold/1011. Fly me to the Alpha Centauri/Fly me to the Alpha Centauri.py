import sys

test_cnt = int(sys.stdin.readline())
for i in range(test_cnt):
    x, y = map(int, sys.stdin.readline().split())

    distance = y - x
    cnt = 0
    now = 0
    mv_distance = 0

    while now < distance:
        cnt += 1
        if cnt % 2 == 1:
            mv_distance += 1
        now += mv_distance

    sys.stdout.write(str(cnt)+'\n')