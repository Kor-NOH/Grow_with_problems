import sys
import heapq

def dijkstra(start_node):
    q = []
    distance[start_node] = 0
    heapq.heappush(q, (0, start_node))

    while q:
        dis, n = heapq.heappop(q)

        if distance[n] < dis:
            continue

        for i in graph[n]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

node_cnt, node_line_cnt = map(int, sys.stdin.readline().split())
start_node = int(sys.stdin.readline())

INF = int(1e9)
distance = [INF] * (node_cnt+1)
graph = [[] for i in range(node_cnt+1)]

for i in range(node_line_cnt):
    sn, en, l = map(int, sys.stdin.readline().split())
    graph[sn].append([en, l])

dijkstra(start_node)

for i in range(1, node_cnt+1):
    if distance[i] == INF:
        sys.stdout.write('INF'+'\n')
    else:
        sys.stdout.write(str(distance[i])+'\n')