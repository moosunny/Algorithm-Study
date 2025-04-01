import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 각 치킨집 위치
chicken = [(x,y) for x in range(n) for y in range(n) if graph[x][y] == 2]
home = [(x,y) for x in range(n) for y in range(n) if graph[x][y] == 1]

def calculate_distance(chicken):
    distance_list = []
    for h in home:
        dist_list = []
        for chick in chicken:
            dist_list.append(abs(h[0] - chick[0]) + abs(h[1] - chick[1]))
        distance_list.append(min(dist_list))


    return sum(distance_list)
    

min_distance = 9999
for combo in combinations(chicken, m):
    if min_distance > calculate_distance(combo):
        min_distance = calculate_distance(combo)

print(min_distance)
    
