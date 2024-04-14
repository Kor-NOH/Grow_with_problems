import sys
import heapq

def dijkstra(s_node, size):
    q = []
    heapq.heappush(q, (0, s_node))
    distance[s_node] = 0

    while q:
        dis, n = heapq.heappop(q)

        if distance[n] < dis:
            continue

        for i in graph[n]:
            cost = dis + i[1]
            if i[0] != size-1 and sight_list[i[0]] == 0:
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

            if i[0] == size-1:
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

n, road_cnt = map(int, sys.stdin.readline().split())
sight_list = list(map(int, sys.stdin.readline().split()))

INF = sys.maxsize
distance = [INF] * n
graph = [[] for i in range(n)]

for i in range(road_cnt):
    n1, n2, l = map(int, sys.stdin.readline().split())
    graph[n1].append([n2, l])
    graph[n2].append([n1, l])

dijkstra(0, n)

if distance[-1] == INF:
    sys.stdout.write('-1')
else:
    sys.stdout.write(str(distance[n-1]))