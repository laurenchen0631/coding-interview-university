
"""
s is vertex
adj[s] is all neighbors of s
"""


def BFS(s, adj):
    level = {s: 0}  # store vertex if it has been visited
    parent = {s: None}
    i = 1
    frontier = [s]  # level i-1
    while frontier:
        next = []  # level i
        for u in frontier:
            for v in adj[u]:
                if v not in level:
                    level[v] = i
                    parent[v] = u
                    next.append(v)
        frontier = next
        i += 1
    return parent


# path from s ----> v
def shortest_path(s, v):
    parent = BFS(s, adj)

    distance = 0
    path = []
    while v is not s:
        path.append(v)
        v = parent[v]
        distance += 1
    path = path.reverse()
    # distance == level[v]

    return path
