import sys
import math

song_cnt, avg = map(int, sys.stdin.readline().split())
sys.stdout.write(str(math.ceil((avg-1+0.01) * song_cnt)))