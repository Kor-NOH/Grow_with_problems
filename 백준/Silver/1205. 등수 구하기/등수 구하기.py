import sys

n, TS, p = map(int, sys.stdin.readline().split())
score_list = list(map(int, sys.stdin.readline().split()))
prize_list = []
cnt = 0

for num in score_list:
    if num >= TS:
        prize_list.append(num)
    else:
        break

if len(prize_list) >= p:
    sys.stdout.write('-1')
else:
    for i in range(-1, (len(prize_list)+1)*-1, -1):
        if prize_list[i] == TS:
            cnt += 1
        else:
            break

    sys.stdout.write(str(len(prize_list)+1-cnt))