from graph_example import UDG1_matrix, UDG2_matrix
from collections import deque


def is_bipartite(graph):
    vertices = list(graph.vertices)
    colorings = {}
    to_visit = deque()

    for vertex in vertices:
        if vertex not in colorings:
            to_visit.append(vertex)
            colorings[vertex] = 1

        while len(to_visit):
            v = to_visit.popleft()
            for neighbor in graph.neighbors(v):
                if neighbor not in colorings:
                    colorings[neighbor] = -colorings[v]
                    to_visit.append(neighbor)
                elif colorings[neighbor] == colorings[v]:
                    return False
    return True


g = UDG1_matrix()
print(is_bipartite(g))

g2 = UDG2_matrix()
print(is_bipartite(g2))
