from contains_cycle import contains_cycle
from list_graph import ListGraph


def topological_sort(graph):
    assert(not contains_cycle(graph))
    STATUS_DISCOVERD = 1
    STATUS_PROCESSED = 2
    order = []
    status = {}

    for vertex in graph.vertices:
        to_visit = [vertex]
        while to_visit:
            v = to_visit.pop()

            if v in status:
                if status[v] == STATUS_DISCOVERD:
                    status[v] = STATUS_PROCESSED
                    order.append(v)
            else:
                status[v] = STATUS_DISCOVERD
                to_visit.append(v)

            for neighbor in graph.neighbors(v):
                if neighbor not in status:
                    to_visit.append(neighbor)

    order.reverse()
    return order


g = ListGraph(True)
for i in range(9):
    g.add_vertex(i)
g.add_edge(0, 1)
g.add_edge(0, 5)
g.add_edge(1, 2)
g.add_edge(2, 4)
g.add_edge(2, 6)
g.add_edge(3, 2)
g.add_edge(5, 8)
g.add_edge(6, 5)
g.add_edge(7, 5)

print(topological_sort(g))
