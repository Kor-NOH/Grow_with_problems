import sys

test_cnt = int(sys.stdin.readline())

for _ in range(test_cnt):
    input_list = list(sys.stdin.readline().split())
    num = float(input_list[0])
    for i in range(1, len(input_list)):
        if input_list[i] == '@':
            num *= 3
        elif input_list[i] == '%':
            num += 5
        else:
            num -= 7

    sys.stdout.write(str(f"{num:.2f}") + '\n')