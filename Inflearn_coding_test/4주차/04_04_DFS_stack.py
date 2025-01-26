graph = {
    1: [2, 5, 9],
    2: [1, 3],
    3: [2, 4],
    4: [3],
    5: [1, 6, 8],
    6: [5, 7],
    7: [6],
    8: [5],
    9: [1, 10],
    10: [9]
}

# 1. 시작 노드를 스택에 넣습니다.
# 2. 현재 스택에 노드를 빼서 visited에 추가합니다.
# 3. 현재 방문한 노드와 인접한 노드 중 방문하지 않은 노드를 스택에 추가합니다.
# 위의 과정을 스택에 빌 때까지 반복

def dfs_stack(adjacent_graph, start_node):
    # 구현해보세요!
    stack = [start_node]
    visited = []
    while stack: # 스택이 비지 않을 때까지
        current_node = stack.pop()
        visited.append(current_node)
        for adjacent_node in adjacent_graph[current_node]:
            if adjacent_node not in visited:
                stack.append(adjacent_node)


    return  visited


print(dfs_stack(graph, 1))  # 1 이 시작노드입니다!
# [1, 9, 10, 5, 8, 6, 7, 2, 3, 4] 이 출력되어야 합니다!