import sys

cnt = int(sys.stdin.readline())
stack = []
stack_high_num = 0
result = []
can = 'YES'

for _ in range(cnt):
    num = int(sys.stdin.readline())

    if num > stack_high_num :
        for i in range(stack_high_num+1, num+1):
            stack.append(i)
            result.append('+')
        stack_high_num = num

        stack.pop()
        result.append('-')

    else :
        if num in stack:
            for i in range(len(stack)):
                if stack[-1] == num:
                    stack.pop()
                    result.append('-')
                    break
                else:
                    stack.pop()
                    result.append('-')


        else:
            can = 'NO'
    # print(stack)
    # print(result)

if can == 'YES':
    for _ in range(len(result)):
        sys.stdout.write(str(result[_]))
        if _ != len(result)-1:
            sys.stdout.write('\n')
else:
    sys.stdout.write('NO')