import sys
from collections import deque


n, L, R = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# print(graph)

# 모든 인접한 나라 간의 인구 수 차이를 계산 -> 연합 국가 개수 도출 -> bfs 알고리즘
# 모든 인접한 나라(연합 국가) 인구 합 / 연합 국가 개수 -> 인구 조정
# 인구 이동이 발생한 

dx = [0,0,-1,1]
dy = [-1,1,0,0]


def bfs(graph, visited, x, y): # graph, 탐색 시작 국가 위치
    visited[x][y] = 1
    queue = deque()
    queue.append([x,y])

    nation_list = [[x,y]]
    population = graph[x][y]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and L <= abs(graph[x][y] - graph[nx][ny]) <= R:
                if visited[nx][ny] == -1:
                    queue.append([nx, ny])
                    visited[nx][ny] = 1
                    nation_list.append([nx,ny])
                    population += graph[nx][ny]

    return nation_list, population

cnt = 0

while True:
    move = False
    visited = [[-1]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j] == -1:
                nations, populations = bfs(graph, visited, i, j)
                if len(nations) > 1:
                    move = True
                    n_pop = populations // len(nations)

                    for x, y in nations:
                        graph[x][y] = n_pop
    if not move:
        break
    cnt += 1

print(cnt)
                
                




