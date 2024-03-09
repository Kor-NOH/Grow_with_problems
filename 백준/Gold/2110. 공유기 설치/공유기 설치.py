import sys
house_cnt, advices = map(int, sys.stdin.readline().split())
house_list, distance = [], []
start, result = 1, 0

for _ in range(house_cnt):
    house_list.append(int(sys.stdin.readline()))

house_list = sorted(house_list)
end = house_list[-1] - house_list[0]

while start <= end:
    mid = (start + end) // 2
    distance.append(house_list[0])

    for house in house_list:
        if house - distance[-1] >= mid:
            distance.append(house)

    if len(distance) >= advices:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
    distance = []

print(result)