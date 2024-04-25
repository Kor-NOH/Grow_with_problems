from collections import deque
import sys

input = sys.stdin.readline
test_cnt = int(input())

def bfs():
    q = deque()  # BFS에 사용할 큐로서 deque를 활용합니다.
    q.append((home_x, home_y))  # 시작 지점인 집을 큐에 추가합니다.
    while q:
        x, y = q.popleft()  # 다음 탐색할 지점을 큐에서 추출합니다.
        if abs(x - festival_x) + abs(y - festival_y) <= 1000:
            return 'happy'  # 축제까지 도달 가능한 경우 'happy'를 반환합니다.
        for i in range(n):  # 편의점을 확인합니다.
            if not visited[i]:  # 아직 방문하지 않은 경우
                new_x, new_y = graph[i]  # 편의점의 좌표를 가져옵니다.
                if abs(x - new_x) + abs(y - new_y) <= 1000:  # 도달 가능한 경우
                    visited[i] = 1  # 방문 표시를 합니다.
                    q.append((new_x, new_y))  # 큐에 도달 가능한 편의점을 추가합니다.
    return 'sad'  # 축제까지 도달할 수 없는 경우 'sad'를 반환합니다.

for _ in range(test_cnt):
    n = int(input())  # 편의점 개수를 입력받습니다.
    home_x, home_y = map(int, input().split())  # 집의 좌표를 입력받습니다.
    graph = []  # 편의점의 좌표를 저장할 리스트입니다.
    for _ in range(n):
        x, y = map(int, input().split())  # 편의점의 좌표를 입력받습니다.
        graph.append((x, y))  # 편의점의 좌표를 그래프에 추가합니다.
    festival_x, festival_y = map(int, input().split())  # 축제의 좌표를 입력받습니다.
    visited = [0] * (n + 1)  # 방문한 편의점을 표시할 배열을 초기화합니다.
    print(bfs())  # BFS 탐색 결과를 출력합니다.
