import sys
import copy
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

empty = [(x,y) for x in range(n) for y in range(m) if graph[x][y] == 0]
virus = [(x,y) for x in range(n) for y in range(m) if graph[x][y] == 2]

def bfs(graph):
    queue = deque(virus)

    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    while queue:
        v_position = queue.popleft()
        x = v_position[0]
        y = v_position[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx,ny))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cnt += 1

    return  cnt

answer = -1

for i in range(len(empty)):
    for j in range(i+1, len(empty)):
        for k in range(j+1, len(empty)):
            # _graph = copy.deepcopy(graph)
            _graph = [row[:] for row in graph]
            _graph[empty[i][0]][empty[i][1]] = 1
            _graph[empty[j][0]][empty[j][1]] = 1
            _graph[empty[k][0]][empty[k][1]] = 1
            result = bfs(_graph)
            if answer < result:
                answer = result

print(answer)