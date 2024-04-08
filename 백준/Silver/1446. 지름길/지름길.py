import sys

short_road = []
road_cnt, goal = map(int, sys.stdin.readline().split())

for i in range(road_cnt):
    s, e, l = map(int, sys.stdin.readline().split())
    if e-s > l and e <= goal:
        short_road.append([s, e, l])
short_road.sort()

dp = [i for i in range(goal+1)]
for i in range(goal+1):
    dp[i] = min(dp[i-1]+1, dp[i])
    for j in range(len(short_road)):
        if short_road[j][0] == i:
            dp[short_road[j][1]] = min(dp[i]+short_road[j][2], dp[short_road[j][1]])

# print(short_road)
# print(dp)
sys.stdout.write(str(dp[goal]))