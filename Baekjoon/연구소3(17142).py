import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

virus = [(x,y) for x in range(n) for y in range(n) if graph[x][y] == 2]

def bfs(graph):
    live_virus = [(x,y) for x in range(n) for y in range(n) if graph[x][y] == "*"]
    queue = deque(live_virus)

    


answer = 9999
# for i in range(len(virus)):
#     for j in range(i+1, len(virus)):
#         for s in range(j+1, len(virus)):
#             _graph = [row[:] for row in graph]
#             _graph[virus[i][0]][virus[i][0]] = '*'
#             _graph[virus[j][0]][virus[j][0]] = '*'
#             _graph[virus[s][0]][virus[s][0]] = '*'
#             result =             

def activate_virus(start, path):
    if len(path) == m:
        # 그래프 복사
        _graph = [row[:] for row in graph]
        
        # 모든 바이러스 위치 초기화 (비활성화 상태)
        for x, y in virus:
            _graph[x][y] = 0
        
        # 선택된 바이러스만 활성화
        for x, y in path:
            _graph[x][y] = 2

        # 활성화된 바이러스 위치 출력
        print("활성화된 바이러스:", path)

        # 이후 여기에 시뮬레이션 코드 등 넣으면 됨
        return

    for i in range(start, len(virus)):
        activate_virus(i + 1, path + [virus[i]])

# 시작
activate_virus(0, [])
