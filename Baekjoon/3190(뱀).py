import sys
from collections import deque
# input = sys.stdin.readline()

n = int(sys.stdin.readline())  # 보드 크기
k = int(sys.stdin.readline())  # 사과 개수

graph = [[0]*n for _ in range(n)]

for _ in range(k):
    x, y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1 

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 

def turn(direction, c):
    if c == 'L':
        return (direction - 1) % 4
    else: 
        return (direction + 1) % 4

l = int(sys.stdin.readline())
rotate = dict()
for _ in range(l):
    x, c = sys.stdin.readline().split()
    rotate[int(x)] = c

def bfs():
    x, y = 0, 0
    graph[x][y] = 2  
    direction = 0  
    time = 0
    q = deque()
    q.append((x, y))

    while True:
        time += 1
        dx, dy = directions[direction]
        nx, ny = x + dx, y + dy


        if not (0 <= nx < n and 0 <= ny < n) or graph[nx][ny] == 2:
            print(time)
            return

        if graph[nx][ny] == 0:
            tx, ty = q.popleft()
            graph[tx][ty] = 0


        graph[nx][ny] = 2
        q.append((nx, ny))
        x, y = nx, ny

        if time in rotate:
            direction = turn(direction, rotate[time])

bfs()
