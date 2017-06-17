from list_graph import ListGraph
from matrix_graph import MatrixGraph


def graph_1(g):
    for i in range(9):
        g.add_vertex(i)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(1, 7)
    g.add_edge(3, 7)
    g.add_edge(7, 8)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(6, 8)
    return g


def UDG1_matrix():
    g = MatrixGraph(False)
    return graph_1(g)


def UDG1_list():
    g = ListGraph(False)
    return graph_1(g)


def graph_2(g):
    for i in range(8):
        g.add_vertex(i)
    g.add_edge(0, 1)
    g.add_edge(0, 5)
    g.add_edge(2, 1)
    g.add_edge(2, 3)
    g.add_edge(2, 5)
    g.add_edge(4, 3)
    g.add_edge(4, 5)
    g.add_edge(4, 7)
    g.add_edge(6, 7)
    return g


def UDG2_matrix():
    g = MatrixGraph(False)
    return graph_2(g)


def UDG2_list():
    g = ListGraph(False)
    return graph_2(g)
