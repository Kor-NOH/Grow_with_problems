import sys
input = sys.stdin.readline

t  = int(input().split()[-1])
for _ in range(t):
    l, n = map(int, input().split())
    stick = [0 for _ in range(l+1)]
    ants = [int(input().split()[-1]) for _ in range(n)]
    f_ant = 0
    l_ant = 0
    for i in ants:
        if i > l-i:
            if f_ant < l-i:
                f_ant = l-i
            if l_ant < i:
                l_ant = i
        else:
            if f_ant < i:
                f_ant = i
            if l_ant < l-i:
                l_ant = l-i
    print(f_ant,l_ant)