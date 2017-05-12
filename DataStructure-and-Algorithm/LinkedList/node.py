class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        if type(node) is Node:
            self.__next = node
        elif node is None:
            self.__next = None
