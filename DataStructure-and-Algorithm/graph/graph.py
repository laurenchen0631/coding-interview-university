class Graph:
    def __init__(self, directed=False):
        self.__directed = directed
        self.vertex_data = {}
        self.edge_data = {}

    @property
    def directed(self):
        return self.__directed

    # tests whether there is an edge from the vertex x to the vertex y;
    def adjacent(self, v1, v2):
        pass

    # lists all vertices y such that
    # there is an edge from the vertex x to the vertex y;
    def neighbors(self, v):
        pass

    # adds the vertex x, if it is not there;
    def add_vertex(self, v):
        pass

    # removes the vertex x, if it is there;
    def remove_vertex(self, v):
        pass

    # adds the edge from the vertex x to the vertex y, if it is not there;
    def add_edge(self, v1, v2):
        pass

    # removes the edge from the vertex x to the vertex y, if it is there;
    def remove_edge(self, v1, v2):
        pass

    # returns the value associated with the vertex x;
    def get_vertex_value(self, v):
        if v in self.vertex_data:
            return self.vertex_data[v]

    # sets the value associated with the vertex x to v.
    def set_vertex_value(self, v, data):
        self.vertex_data[v] = data

    # returns the value associated with the edge (x, y);
    def get_edge_value(self, v1, v2):
        if (v1, v2) in self.edge_data:
            return self.edge_data[(v1, v2)]
        return None

    # sets the value associated with the edge (x, y) to v.
    def set_edge_value(self, v1, v2, data):
        self.edge_data[(v1, v2)] = data


