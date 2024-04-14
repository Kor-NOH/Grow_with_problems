import sys
import heapq

def dijkstra(start_city):
    q = []
    distance[start_city][0] = 0
    distance[start_city][1] = [start_city]
    heapq.heappush(q, (0, start_city))

    while q:
        dis, now = heapq.heappop(q)

        if distance[now][0] < dis:
            continue

        for next_city, cost in graph[now]:
            new_cost = dis + cost
            if new_cost < distance[next_city][0]:
                distance[next_city][0] = new_cost
                distance[next_city][1] = distance[now][1] + [next_city]  # Append next_city instead of now
                heapq.heappush(q, (new_cost, next_city))

city_cnt = int(sys.stdin.readline())
bus_cnt = int(sys.stdin.readline())
graph = [[] for _ in range(city_cnt+1)]
INF = int(1e9)

for _ in range(bus_cnt):
    start_city, end_city, cost = map(int, sys.stdin.readline().split())
    graph[start_city].append((end_city, cost))

start_city, end_city = map(int, sys.stdin.readline().split())

distance = [[INF, []] for _ in range(city_cnt+1)]

dijkstra(start_city)

sys.stdout.write(str(distance[end_city][0])+'\n')
sys.stdout.write(str(len(distance[end_city][1]))+'\n')
sys.stdout.write(' '.join(map(str, distance[end_city][1])))