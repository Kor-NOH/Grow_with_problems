import sys

cnt = int(sys.stdin.readline())
for _ in range(cnt):
    input_list = list(map(int, sys.stdin.readline().split()))
    result = 0

    for i in range(1, 21):
        for j in range(i+1, 21):
            if input_list[i] > input_list[j]:
                result += 1
                
    sys.stdout.write(str(input_list[0])+' ')
    sys.stdout.write(str(result)+'\n')