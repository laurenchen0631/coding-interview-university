from graph_example import UDG1_matrix, UDG2_list


def dfs_recursive(graph, start):
    parents = {start: None}

    def dfs_utils(vertex):
        nonlocal parents
        for v in graph.neighbors(vertex):
            if v not in parents:
                parents[v] = vertex
                dfs_utils(v)

    dfs_utils(start)
    return parents


def dfs_iterative(graph, start):
    parents = {start: None}
    to_visit = [start]
    while to_visit:
        v = to_visit.pop()
        for neighbor in graph.neighbors(v):
            if neighbor not in parents:
                parents[neighbor] = v
                to_visit.append(neighbor)
    return parents


g1 = UDG1_matrix()
g2 = UDG2_list()
print(dfs_iterative(g1, 0))
print(dfs_recursive(g1, 0))
print(dfs_iterative(g2, 0))
print(dfs_recursive(g2, 0))
