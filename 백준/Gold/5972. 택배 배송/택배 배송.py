import sys
import heapq

def dijkstra(s_node):
    q = []
    distance[s_node] = 0
    heapq.heappush(q, (0, s_node))

    while q:
        dis, n = heapq.heappop(q)

        if distance[n] < dis:
            continue

        for i in graph[n]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

node_cnt, road_cnt = map(int, sys.stdin.readline().split())
INF = int(1e9)
distance = [INF] * (node_cnt+1)
graph = [[] for i in range(node_cnt+1)]

for i in range(road_cnt):
    n1, n2, l = map(int, sys.stdin.readline().split())
    graph[n1].append([n2, l])
    graph[n2].append([n1, l])

dijkstra(1)

sys.stdout.write(str(distance[-1]))