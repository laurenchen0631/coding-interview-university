from graph import Graph


class MatrixGraph(Graph):
    def __init__(self, directed=False):
        super().__init__(directed)
        self.__label_index = {}
        self.__graph = []

    def __vertex_index(self, v):
        if v in self.__label_index:
            self.__label_index[v]
        return None

    @property
    def vertices(self):
        return self.__label_index.keys()

    def add_vertex(self, v):
        if v in self.__label_index:
            return

        self.__label_index[v] = len(self.__label_index)
        for row in self.__graph:
            row.append(False)
        self.__graph.append([False] * len(self.__label_index))
        return self

    def remove_vertex(self, v):
        if v not in self.__label_index:
            return

        index = self.__label_index[v]
        del self.__label_index[v]
        for label in self.__label_index:
            if self.__label_index[label] > index:
                self.__label_index[label] -= 1
        self.__graph.pop(index)
        for row in self.__graph:
            row.pop(index)
        return self

    def add_edge(self, v1, v2):
        if v1 not in self.__label_index or v2 not in self.__label_index:
            return
        v1 = self.__label_index[v1]
        v2 = self.__label_index[v2]
        self.__graph[v1][v2] = True
        if not self.directed:
            self.__graph[v2][v1] = True
        return self

    def remove_edge(self, v1, v2):
        if v1 not in self.__label_index or v2 not in self.__label_index:
            return

        v1 = self.__label_index[v1]
        v2 = self.__label_index[v2]
        self.__graph[v1][v2] = False
        if not self.directed:
            self.__graph[v2][v1] = False
        return self

    def adjacent(self, v1, v2):
        if v1 not in self.__label_index or v2 not in self.__label_index:
            return False

        v1 = self.__label_index[v1]
        v2 = self.__label_index[v2]

        return self.__graph[v1][v2]

    def neighbors(self, v):
        if v not in self.__label_index:
            raise IndexError(str(v) + " is not a vertex in graph")
        adj = []
        index = self.__label_index[v]
        for j in range(len(self.__graph[index])):
            if self.__graph[index][j]:
                adj.append(self.__index_to_label(j))
        return adj

    def __index_to_label(self, index):
        for (label, i) in self.__label_index.items():
            if i == index:
                return label

    def __len__(self):
        return len(self.__graph)

    def __getitem__(self, key):
        return self.neighbors(key)

    def print(self):
        for row in self.__graph:
            print(row)

    def debug(self):
        print(self.__label_index)


if __name__ == "__main__":
    g = MatrixGraph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.debug()
    g.remove_vertex("C")
    g.debug()
    g.add_edge("A", "D")
    g.add_edge("B", "D")
    g.print()
    print(len(g))
    print(g["D"])
    print(g.neighbors("D"))
    g.remove_edge("D", "A")
    g.print()
    print(g.neighbors("D"))
