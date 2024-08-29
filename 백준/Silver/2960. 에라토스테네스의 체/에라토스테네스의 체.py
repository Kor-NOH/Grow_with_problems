import sys

n, k = map(int, sys.stdin.readline().split())
num_list = list(range(2, n+1))
cnt = 0

for _ in range(n):
    a = num_list[0]
    mul_num = 1

    while cnt < k:
        del_num = a * mul_num
        mul_num += 1

        if del_num in num_list:
            num_list.remove(del_num)
            cnt += 1

        if del_num > n:
            break

    if cnt == k:
        break

print(del_num)