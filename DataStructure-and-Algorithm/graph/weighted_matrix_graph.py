from matrix_graph import MatrixGraph


class WeightedMatrixGraph(MatrixGraph):
    def __init__(self, directed=False):
        super().__init__(directed)
        self.__weight = {}

    def add_edge(self, v1, v2, weight=1):
        super().add_edge(v1, v2)
        self.__weight[(v1, v2)] = weight
        if not self.directed:
            self.__weight[(v2, v1)] = weight

    def remove_edge(self, v1, v2):
        super().remove_edge(v1, v2)
        del self.__weight[(v1, v2)]
        if not self.directed:
            del self.__weight[(v2, v1)]

    def update_weight(self, v1, v2, weight):
        if self.adjacent(v1, v2):
            self.__weight[(v1, v2)] = weight
            if not self.directed:
                self.__weight[(v2, v1)] = weight

    def get_weight(self, v1, v2):
        return self.__weight.get((v1, v2), None)
