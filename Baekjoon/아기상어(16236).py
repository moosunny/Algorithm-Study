import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

fish_size = [1,2,3,4,5,6]

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            graph[i][j] = 0
            shark_x, shark_y = i, j

# 조건
# 1. 더 이상 먹을 수 있는 물고기가 없으면 종료
# 2. 먹을 수 있는 물고기가 한마리면 그 물고기를 먹으러 감 -> 물고기 개수를 새는 함수 추가
# 3. 먹을 수 있는 물고기가 1 마리보다 많은 경우, 거리가 가장 가까운 물고기를 먹으러 감 
# -> 먹을 수 있는 물고기 수 계산 -> 거리를 계산 -> 같은 거리에 있는 다수 물고기는(가장 위 -> 가장 왼쪽 순으로) 
# 

# def cal_distance(x,y, fish_list):
#     min_distance = float('inf')
#     distance_list = []
#     for fish in fish_list:
#         distance = abs(x - fish[0]) + abs(y - fish[1])
#         distance_list.append([fish[0], fish[1], distance])
#         if min_distance > distance:
#             min_distance = distance
    
#     next_candidate = []
#     for i in range(len(distance_list)):
#         if min_distance == distance_list[i][2]:
#             next_candidate.append(distance_list[i])

#     if len(next_candidate) < 2:
#         return next_candidate
#     else:
#         max_north = -1
#         max_north_list = []
#         for idx, candidate in enumerate(len(next_candidate)):# 가장 위 물고기
#             if max_north < candidate[idx][0]:
#                 max_north = candidate[idx][0]
#         north_cnt = 0
#         for i in range(len(next_candidate)):
#             if max_north == next_candidate[i][0]:
#                 north_cnt += 1
#         for i in range(len(next_candidate)):
#             if max_north == next_candidate[i][0]:
#                 max_north_list.append(next_candidate)
#         if north_cnt == 1:
#             return max_north_list[0], max_north_list[1]
#         else:
#             max_left = 9999
#             max_left_list = []
#             for idx, candidate in enumerate(len(next_candidate)):# 가장 위 물고기
#                 if max_left > candidate[idx][1]:
#                     max_north = candidate[idx][1]
#             left_cnt = 0
#             for i in range(len(next_candidate)):
#                 if max_left == next_candidate[i][1]:
#                     left_cnt += 1
#             for i in range(len(next_candidate)):
#                 if max_left == next_candidate[i][1]:
#                     max_left_list.append(next_candidate)
#             if len(max_left_list) == 1:
#                 return max_left_list[0], max_left_list[1]

        
#         return print("잘못된 코드 구성")


def bfs(shark_x, shark_y, size, graph):
    visited = [[-1]*n for _ in range(n)]
    queue = deque()
    queue.append([shark_x, shark_y])
    visited[shark_x][shark_y] = 0
    fishes = []


    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == -1:
                if graph[nx][ny] <= size:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx, ny]) # 이동 
                    if 0 < graph[nx][ny] < size: # 만약에 0이 아닌 물고기가 있다면 리스트에 추가
                        # level += graph[nx][ny]
                        fishes.append([visited[nx][ny], nx, ny]) # 시간, x, y
    return sorted(fishes)

size = 2
eat = 0
answer = 0

while True:
    fishes = bfs(shark_x, shark_y, size, graph)
    if not fishes:
        break
    
    shark_x = fishes[0][1]
    shark_y = fishes[0][2]
    
    graph[fishes[0][1]][fishes[0][2]] = 0
    answer += fishes[0][0]
    
    eat += 1
    if size == eat:
        eat = 0
        size += 1

print(answer)

