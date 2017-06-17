from graph import Graph


class ListGraph(Graph):
    def __init__(self, directed=False):
        super().__init__(directed)
        self.__graph = {}

    @property
    def vertices(self):
        return self.__graph.keys()

    def add_vertex(self, v):
        if v in self.__graph:
            return
        self.__graph[v] = []

    def remove_vertex(self, v):
        if v not in self.__graph:
            return
        del self.__graph[v]
        for v2 in self.__graph:
            self.remove_edge(v, v2)

    def add_edge(self, v1, v2):
        if v1 not in self.__graph or v2 not in self.__graph:
            return
        self.__graph[v1].append(v2)
        if not self.directed:
            self.__graph[v2].append(v1)

    def remove_edge(self, v1, v2):
        if v1 not in self.__graph or v2 not in self.__graph:
            return

        for i in range(len(self.__graph[v1])):
            if self.__graph[v1][i] == v2:
                self.__graph[v1].pop(i)
                break
        if not self.directed:
            for i in range(len(self.__graph[v2])):
                if self.__graph[v2][i] == v1:
                    self.__graph[v2].pop(i)

    def adjacent(self, v1, v2):
        if v1 not in self.__graph or v2 not in self.__graph:
            return False

        for v in self.__graph[v1]:
            if v == v2:
                return True
        return False

    def neighbors(self, v):
        if v not in self.__graph:
            raise IndexError

        return self.__graph[v][:]

    def __len__(self):
        return len(self.__graph)

    def __getitem__(self, key):
        return self.neighbors(key)

    def print(self):
        print(self.__graph)


if __name__ == "__main__":
    g = ListGraph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.print()
    g.remove_vertex("C")
    g.print()
    g.add_edge("A", "D")
    g.add_edge("B", "D")
    g.print()
    print(len(g))
    print(g["D"])
    print(g.neighbors("D"))
    g.remove_edge("D", "A")
    g.print()
    print(g.neighbors("D"))
