import sys
import heapq

def dijkstra(s_node, e_node, stu_cnt):
    distance = [INF] * (stu_cnt+1)
    q = []
    heapq.heappush(q, (0, s_node))
    distance[s_node] = 0

    while q:
        dis, n = heapq.heappop(q)

        if distance[n] < dis:
            continue

        for i in graph[n]:
            cost = dis + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[e_node]


student_cnt, road_cnt, destination = map(int, sys.stdin.readline().split())

graph = [[] for i in range(student_cnt+1)]
INF = int(1e9)
student_cost = []

for i in range(road_cnt):
    s_city, e_city, l = map(int, sys.stdin.readline().split())
    graph[s_city].append([e_city, l])

for i in range(1, student_cnt+1):
    road_sum = dijkstra(i, destination, student_cnt)
    road_sum += dijkstra(destination, i, student_cnt)

    student_cost.append(road_sum)

sys.stdout.write(str(max(student_cost)))