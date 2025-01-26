from collections import deque

graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}

# 1. 시작 노드를 큐에 넣습니다.
# 2, 현재 큐의 노드를 빼서 visited에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 큐에 추가합니다.

def bfs_queue(adj_graph, start_node):
    queue = deque([start_node])
    visited = []
    while queue:
        current_node = queue.popleft()
        visited.append(current_node)
        for adg_node in adj_graph[current_node]:
            if adg_node not in visited:
                queue.append(adg_node)
    return  visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!