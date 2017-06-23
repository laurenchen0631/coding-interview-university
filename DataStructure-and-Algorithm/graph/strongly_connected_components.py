from list_graph import ListGraph


def easy_SCC(graph):
    # Runtime: O(|V|^2 + |V|*|E|)
    # for each vertex v
    #   explore v to determine vertices reachable from v
    reachable_from = {}
    for vertex in graph.vertices:
        to_visit = [vertex]
        reachable_from[vertex] = set()
        while to_visit:
            v = to_visit.pop()
            reachable_from[vertex].add(v)
            for neighbor in graph.neighbors(v):
                if neighbor not in reachable_from[vertex]:
                    to_visit.append(neighbor)
    # for each vertex v
    #   find u reachable from v that can also reach v
    components = []
    is_scc = {}
    for vertex in graph.vertices:
        if vertex in is_scc:
            continue
        components.append([])
        for u in reachable_from[vertex]:
            if vertex in reachable_from[u]:
                components[-1].append(u)
                is_scc[u] = True
    return components


def SCC(graph):
    def reverse(graph):
        reversed_graph = type(graph)(directed=True)
        for vertex in graph.vertices:
            reversed_graph.add_vertex(vertex)
            for neighbor in graph.neighbors(vertex):
                reversed_graph.add_vertex(neighbor)
                reversed_graph.add_edge(neighbor, vertex)
        return reversed_graph

    # Runtine: O(|V| + |E|)
    # run dfs of reversed graph
    entry_time = {}
    exit_time = {}
    time = 0
    reversed_graph = reverse(graph)
    for vertex in reversed_graph.vertices:
        if vertex in entry_time:
            continue
        to_visit = [vertex]
        while to_visit:
            v = to_visit.pop()
            time += 1
            print(time, v)
            if v not in entry_time:
                entry_time[v] = time
                to_visit.append(v)
            else:
                exit_time[v] = time
                continue

            for neighbor in reversed_graph.neighbors(v):
                if neighbor not in entry_time:
                    to_visit.append(neighbor)

    # for v in reverse exit time order
    visited = {}
    components = []
    for v, _ in reversed(sorted(list(exit_time.items()), key=lambda x: x[1])):
        # if not visted(v)
        if v in visited:
            continue
        # explore v
        to_visit = [v]
        components.append([v])
        visited[v] = True
        while to_visit:
            v = to_visit.pop()
            for neighbor in graph.neighbors(v):
                # mark visited vertices as new SCC
                if neighbor not in visited:
                    visited[neighbor] = True
                    components[-1].append(neighbor)
                    to_visit.append(neighbor)
    return components


def create_graph():
    graph = ListGraph(directed=True)
    for i in range(12):
        graph.add_vertex(i)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(3, 2)
    graph.add_edge(2, 1)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)
    graph.add_edge(3, 5)
    graph.add_edge(7, 5)
    graph.add_edge(8, 10)
    graph.add_edge(10, 11)
    graph.add_edge(11, 9)
    graph.add_edge(9, 8)
    return graph


g = create_graph()
print(SCC(g))
