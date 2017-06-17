def contains_cycle(graph):
    STATUS_DISCOVERD = 1
    STATUS_PROCESSED = 2

    for vertex in graph.vertices:
        status = {}
        to_visit = [vertex]
        while to_visit:
            v = to_visit.pop()

            if v in status:
                if status[v] == STATUS_DISCOVERD:
                    status[v] = STATUS_PROCESSED
            else:
                status[v] = STATUS_DISCOVERD
                to_visit.append(v)

            for neighbor in graph.neighbors(v):
                if neighbor in status:
                    if status[neighbor] == STATUS_DISCOVERD:
                        return True
                else:
                    to_visit.append(neighbor)
    return False
