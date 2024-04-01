import sys

input_num = int(sys.stdin.readline())

if input_num == 1:
    sys.stdout.write('0')

else:
    decimal_check_list = [1] * (input_num+1)
    decimal_list = []
    decimal_check_list[0], decimal_check_list[1] = 0, 0
    result = 0
    for i in range(2, input_num+1):
        mul_num = 3
        if decimal_check_list[i] == 1:
            decimal_list.append(i)
            num = i*2

            while num < (input_num+1):
                decimal_check_list[num] = 0
                num = i * mul_num
                mul_num += 1


    start_num, end_num = 0, 1
    s = decimal_list[0]
    while start_num <= end_num:
        if s == input_num:
            result += 1

        if s < input_num:
            if end_num == len(decimal_list):
                break
            s += decimal_list[end_num]
            end_num += 1

        elif s >= input_num:
            if start_num == (len(decimal_list)-1):
                break
            s -= decimal_list[start_num]
            start_num += 1

            if start_num >= len(decimal_list):
                break

    sys.stdout.write(str(result))