import sys

cnt = int(sys.stdin.readline())
s = set()

for _ in range(cnt):
    order_list = list(sys.stdin.readline().split())
    order = order_list[0]
    if len(order_list) == 2:
        num = order_list[1]

    if order == 'add':
        s.add(int(num))
    elif order == 'remove':
        s.discard(int(num))
    elif order == 'check':
        if int(num) in s:
            sys.stdout.write('1'+'\n')
        else:
            sys.stdout.write('0'+'\n')
    elif order == 'toggle':
        if int(num) in s:
            s.remove(int(num))
        else:
            s.add(int(num))
    elif order == 'all':
        s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
    else:
        s.clear()