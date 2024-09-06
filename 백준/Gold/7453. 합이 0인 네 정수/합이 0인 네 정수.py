# 합이 0인 네 정수
import sys
N = int(sys.stdin.readline())

A, B, C, D = [], [], [], []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

A_B = []
for a in A:
    for b in B:
        A_B.append(a+b)
A_B.sort()

C_D = []
for c in C:
    for d in D:
        C_D.append(c+d)
C_D.sort()

result = 0
left, right = 0, len(A_B)-1
s = 0

while 0 <= right and left < len(A_B):
    s = A_B[left] + C_D[right]
    if s < 0:
        left += 1
    elif s > 0:
        right -= 1
    else:
        x = 1
        for i in range(left+1, len(A_B)):
            if A_B[left] == A_B[i]:
                x += 1
            else:
                break
        y = 1
        for i in range(right-1, -1, -1):
            if C_D[right] == C_D[i]:
                y += 1
            else:
                break
        result += x*y
        left += x
        right -= y

print(result)