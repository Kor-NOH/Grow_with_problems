import sys

z_size = int(sys.stdin.readline().strip())
a, b, c = 1, 1, 1

for i in range(1, z_size):
    a, b, c = (a + b + c) % 9901, (a + c) % 9901, (a + b) % 9901

sys.stdout.write(str((a + b + c) % 9901))