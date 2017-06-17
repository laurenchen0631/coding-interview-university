from collections import deque


def list_to_incidence_matrix(l):
    num_of_vertex = len(l)
    matrix = [[] for _ in range(num_of_vertex)]
    for v1 in range(num_of_vertex):
        for v2 in l[v1]:
            if v1 > v2:  # undirected
                for i in range(num_of_vertex):
                    matrix[i].append(0)
                matrix[v1][-1] = 1
                matrix[v2][-1] = 1
    return matrix


def BFS(matrix, start):
    discoverd = [False] * len(matrix)
    parent = [-1] * len(matrix)
    q = deque()
    q.append(start)
    discoverd[start] = True
    while len(q):
        v = q.popleft()
        for v2 in range(len(matrix)):
            if matrix[v][v2]:
                if not discoverd[v2]:
                    q.append(v2)
                    discoverd[v2] = True
                    parent[v2] = v
    return parent
