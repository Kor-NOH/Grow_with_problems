import sys

city_cnt = int(sys.stdin.readline())
road_l = list(map(int, sys.stdin.readline().split()))
oil_price = list(map(int, sys.stdin.readline().split()))
result = oil_price[0] * road_l[0]


for i in range(1, city_cnt-1):
    result += min(oil_price[:i+1]) * road_l[i]

sys.stdout.write(str(result))