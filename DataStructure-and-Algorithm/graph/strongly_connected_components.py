from list_graph import ListGraph


def easy_SCC(graph):
    # Runtime: O(|V|^2 + |V|*|E|)
    # for each vertex v
    #   explore v to determine vertices reachable from v
    reachable_from = {}
    for vertex in graph.vertices:
        to_vistt = [vertex]
        reachable_from[vertex] = set()
        while to_visit:
            v = to_visit.pop()
            reachable_from[vertex].add(v)
            for neighbor in graph.neighbors(v):
                if neighbor not in reachable_from[vertex]:
                    to_visit.append(neighbor)
    print(reachable_from)

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
        revered_graph = type(graph)()
        for vertex in graph.vertices:
            revered_graph.add_vertex(vertex)
            for neighbor in graph.neighbors(graph):
                reversed_graph.add_vertex(neighbor)
                revered_graph.add_edge(neighbor, vertex)

    # Runtine: O(|V| + |E|)
    # run dfs of reversed graph
    entry_time = {}
    exit_time = {}
    time = 0
    revered_graph = reverse(graph)
    for vertex in reversed_graph.vertices:
        to_visit = [vertex]
        while to_visit:
            v = to_visit.pop()
            time += 1
            if v not entry_time:
                entry_time[v] = time
                to_visit.append(v)
            else:
                exit_time[v] = time
                continue

            for neighbor in revered_graph.neighbors(v):
                if neighbor not in entry_time:
                    to_visit.append(neighbor)

    # for v in reverse exit time order
    visited = {}
    components = []
    for v in reversed(sorted(list(exit_time.items()), key=lambda x: x[1])):
        # if not visted(v)
        if v in visited:
            continue
        # explore v
        to_visit = [v]
        SCC.append([v])
        while to_visit:
            for neighbor in graph.neighbors(v):
                # mark visited vertices as new SCC
                if neighbor not in visited:
                    visited[neighbor] = True
                    components[-1].append(neighbor)
                    to_visit.append(neighbor)
    return components
