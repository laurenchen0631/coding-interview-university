from collections import deque


def count_connected_components(graph):
    assert(not graph.directed)

    visited = {}
    counter = 0
    for vertex in graph.vertices:
        if vertex in visited:
            continue
        counter += 1
        to_vistit = deque()
        to_vistit.append(vertex)
        while len(to_vistit):
            v = to_vistit.popleft()
            for neighbor in graph.neighbors(v):
                if neighbor not in visited:
                    visited[neighbor] = True
                    to_visit.append(neighbor)
    return counter
