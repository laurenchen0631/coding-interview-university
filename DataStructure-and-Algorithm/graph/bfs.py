from graph_example import UDG1_matrix
from collections import deque


def bfs(graph, start):
    parents = {start: None}
    to_visit = deque()
    to_visit.append(start)

    while len(to_visit):
        v = to_visit.popleft()
        for neighbor in graph.neighbors(v):
            if neighbor not in parents:
                parents[neighbor] = v
                to_visit.append(neighbor)
    return parents


g = UDG1_matrix()
print(bfs(g, 0))
