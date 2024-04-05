import sys

def backtracking(num):
    if len(array) == m:
        sys.stdout.write(' '.join(map(str, array))+'\n')

    for i in range(num, n+1):
        if i not in array:
            array.append(i)
            backtracking(i)
            array.pop()

n, m = map(int, sys.stdin.readline().split())

array = []
backtracking(1)