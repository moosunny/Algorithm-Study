import sys


n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cc_list = [(graph[x][y], x, y) for x in range(n) for y in range(m) if 1 <= graph[x][y] < 6]


cctv_1 = [[(1, 0)], [(-1, 0)], [(0, 1)], [(0, -1)]]
cctv_2 = [[(1, 0), (-1, 0)], [(0, 1), (0, -1)]]
cctv_3 = [[(1, 0), (0, 1)], [(0, 1), (-1, 0)], [(0, -1), (-1, 0)], [(1, 0), (0, -1)]]
cctv_4 = [[(1, 0), (0, 1), (-1, 0)], [(0, 1), (-1, 0), (0, -1)],
          [(-1, 0), (0, -1), (1, 0)], [(0, -1), (1, 0), (0, 1)]]
cctv_5 = [[(1, 0), (0, 1), (-1, 0), (0, -1)]]

cctv_types = {1: cctv_1, 2: cctv_2, 3: cctv_3, 4: cctv_4, 5: cctv_5}

def move(graph, x, y, directions, record):
    for dx, dy in directions:
        nx, ny = x, y
        while True:
            nx += dx
            ny += dy
            if not (0 <= nx < n and 0 <= ny < m):  
                break
            if graph[nx][ny] == 6: 
                break
            if graph[nx][ny] == 0:  
                graph[nx][ny] = "#"  
                record.append((nx, ny))  


def dfs(depth):
    global min_blind_spots

    if depth == len(cc_list): 
        count_blind_spots()
        return

    cctv_type, x, y = cc_list[depth]
    for directions in cctv_types[cctv_type]:  
        record = [] 
        move(graph, x, y, directions, record) 
        dfs(depth + 1) 
        for nx, ny in record: 
            graph[nx][ny] = 0


def count_blind_spots():
    global min_blind_spots
    blind_spots = sum(row.count(0) for row in graph)
    min_blind_spots = min(min_blind_spots, blind_spots)


min_blind_spots = sys.maxsize
dfs(0)

print(min_blind_spots)
