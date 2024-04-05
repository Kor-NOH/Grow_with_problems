import sys

def backtracking():
    if len(array) == m:
        sys.stdout.write(' '.join(map(str, array))+'\n')

    for i in range(1, n+1):
        if len(array) != m:
            array.append(i)
            backtracking()
            array.pop()

n, m = map(int, sys.stdin.readline().split())
array = []

backtracking()