import sys
import math

song_cnt, avg = map(int, sys.stdin.readline().split())
avg = avg - 1 + 0.01
sys.stdout.write(str(math.ceil(avg * song_cnt)))