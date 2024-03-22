import sys

num = int(sys.stdin.readline())
n = 2
result_list = []

for _ in range(num):
    if num == 1:
        break

    if num % n == 0:
        result_list.append(n)
        num //= n
    else:
        n += 1

for result in result_list:
    print(result)