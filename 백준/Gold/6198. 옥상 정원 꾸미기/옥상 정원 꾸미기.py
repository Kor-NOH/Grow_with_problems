import sys

building_cnt = int(sys.stdin.readline())
building = []
stack = []
result = 0

for _ in range(building_cnt):
    b = int(sys.stdin.readline().strip())
    building.append(b)

for b in building:

    while stack and stack[-1] <= b:
        stack.pop()
    stack.append(b)

    result += len(stack)-1


sys.stdout.write(str(result))