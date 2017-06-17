from collections import deque


def matrix_to_list(matrix):
    N = len(matrix)
    adjacency_list = [[] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if matrix[i][j]:
                adjacency_list[i].append(j)
    return adjacency_list


def incidence_matrix_to_list(matrix):
    adjacency_list = [[] for _ in range(len(matrix))]
    for edge in range(len(matrix[0])):
        vertex = []
        for v in range(len(matrix)):
            if matrix[v][edge]:
                vertex.append(v)
            if len(vertex) == 2:
                break
        adjacency_list[vertex[0]].append(vertex[1])
        adjacency_list[vertex[1]].append(vertex[0])
    return adjacency_list


def BFS(adjacency_list, is_directed, start):
    # vertex is precessed after we have traversed all edges from it
    # processed = [False] * len(adjacency_list)
    # vertex is discoverd the first we visit it
    discoverd = [False] * len(adjacency_list)
    parent = [-1] * len(adjacency_list)

    q = deque()
    q.append(start)
    discoverd[start] = True
    while len(q):
        v = q.popleft()
        # processed[v] = True
        # process vertex early
        for v2 in adjacency_list[v]:
            # if not processed[v2] or is_directed:
                # process edge (v, v2) here
                # print(f"processed edge ({v}, {v2})")
                # pass
            if not discoverd[v2]:
                q.append(v2)
                discoverd[v2] = True
                parent[v2] = v
        # process vertex late
        # print("processed vertex ", v)
    return parent


def shortest_path(graph, start, goal):
    if start == goal or goal == -1:
        print(start)
        return

    parent = BFS(graph, False, start)
    path = []
    while goal != -1:
        path.append(str(goal))
        goal = parent[goal]
    print("->".join(reversed(path)))


def is_bipartite(graph):
    # 0 means not colored
    color = [0] * len(graph)

    # bipartitle = True
    discoverd = [False] * len(graph)

    def bfs(start):
        parent = [-1] * len(graph)
        q = deque()
        q.append(start)
        discoverd[start] = True
        while len(q):
            v = q.popleft()
            for v2 in graph[v]:
                if discoverd[v2]:
                    if color[v2] == color[v]:
                        return False
                else:
                    discoverd[v2] = True
                    q.append(v2)
                    color[v2] = -color[v]

    for i in range(len(graph)):
        if not discoverd[i]:
            color[i] = 1
            if not bfs(j):
                return False
    return True


def dfs(graph, start):
    discoverd = [False] * len(graph)
    parent = [-1] * len(graph)
    time = 0
    entry_time = [0] * len(graph)
    exit_time = [0] * len(graph)
    finished = False

    def __dfs(v):
        if finished:
            return
        nonlocal time

        time += 1
        entry_time[v] = time
        discoverd[v] = True
        for v2 in graph[v]:
            if not discoverd[v2]:
                parent[v2] = v
                discoverd[v2] = True
                __dfs(v2)
            else:
                if parent[v] != v2:
                    print("Cycle detected")
                    print(v, v2)

            if finished:
                return
        time += 1
        exit_time[v] = time

    __dfs(start)
    print(entry_time)
    print(exit_time)


def dfs_iterative(graph, start):
    visited = [False] * len(graph)
    stack = [start]
    visited[start] = True

    while len(stack):
        v = stack.pop()
        for v2 in graph[v]:
            if not visited[v2]:
                stack.append(v2)
                visited[v2] = True
        print(v)


g = [
    [1, 4, 5],
    [0, 2, 4],
    [1, 3],
    [2, 4],
    [0, 1, 3],
    [0]
]

# shortest_path(g, 0, 3)
# dfs(g, 0)
dfs_iterative(g, 0)
