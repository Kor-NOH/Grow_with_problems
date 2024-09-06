import sys
import heapq

gas_station_cnt = int(sys.stdin.readline())
station_info = []
result = 0
pos = 0

for i in range(gas_station_cnt):
    d, g = map(int, sys.stdin.readline().split())
    heapq.heappush(station_info, [d, g])

station_info.sort()
# print(station_info)

goal, gas = map(int, sys.stdin.readline().split())
tmp_l = []

while gas < goal:
    cnt = 0
    del_list = []

    for i in range(len(station_info)):
        if station_info[i][0] <= gas:
            heapq.heappush(tmp_l, -station_info[i][1])
            del_list.append(i)
            cnt += 1

    for i in range(cnt):
        del station_info[del_list[i]-i]

    if not tmp_l:
        pos = 1
        break

    add_gas = heapq.heappop(tmp_l)
    result += 1
    gas -= add_gas

if pos == 1:
    print(-1)
else:
    print(result)