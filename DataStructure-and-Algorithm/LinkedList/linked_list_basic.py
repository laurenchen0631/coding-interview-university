from node import Node


class LinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        data = []
        node = self.__head
        while node is not None:
            data.append(str(node.data))
            node = node.next
        return "->".join(data)

    def __len__(self):
        return self.size()

    def __iter__(self):
        node = self.__head
        while node is not None:
            yield node.data
            node = node.next
        raise StopIteration

    def size(self):
        size = 0
        node = self.__head
        while node is not None:
            node = node.next
            size += 1
        return size

    def empty(self):
        return self.__head is None

    def front(self):
        return self.__head.data

    def back(self):
        node = self.__head
        while node.next is not None:
            node = node.next
        return node.data

    def __getitem__(self, key):
        if type(key) is int:
            return self.value_at(key)
        return None

    def value_at(self, index):
        if index < 0:
            return self.value_n_from_end(abs(index))
        node = self.__head
        for _ in range(index):
            if node is None:
                raise IndexError("Error: index out of range")
            node = node.next
        return node.data

    def value_n_from_end(self, n):
        if n < 1 or self.__head is None:
            raise IndexError("Error: index out of range")

        flag_node = self.__head
        for _ in range(n - 1):
            flag_node = flag_node.next
            if flag_node is None:
                raise IndexError("Error: index out of range")

        node = self.__head
        while flag_node.next is not None:
            node = node.next
            flag_node = flag_node.next
        return node.data

    def push_front(self, data):
        node = Node(data, self.__head)
        self.__head = node

    def push_back(self, data):
        if self.__head is None:
            self.push_front(data)
        else:
            node = self.__head
            while node.next is not None:
                node = node.next
            node.next = Node(data)

    def pop_front(self):
        if self.__head is None:
            raise IndexError("Unable to pop from empty list")
        node = self.__head
        self.__head = node.next
        return node.data

    def pop_back(self):
        if self.__head is None:
            raise IndexError("Unable to pop from empty list")

        node = self.__head
        if node.next is None:
            self.__head = None
            return node.data
        else:
            while node.next.next is not None:
                node = node.next
            tail = node.next
            node.next = None
            return tail.data

    def reverse(self):
        if self.__head is None or self.__head.next is None:
            return

        new_list_head = self.__head
        next_node = self.__head.next
        self.__head.next = None
        while next_node is not None:
            node = next_node
            next_node = next_node.next
            node.next = new_list_head
            new_list_head = node

        self.__head = new_list_head

    def __node_before(self, index):
        if index == 0:
            return None

        node = self.__head
        for _ in range(index - 1):
            node = node.next
            if node is None:
                raise IndexError("Error: index out of range")
        return node

    def insert(self, index, data):
        if index < 0:
            raise IndexError("Error: index out of range")
        if index == 0:
            self.push_front(data)
        else:
            prev_node = self.__node_before(index)
            node = Node(data, prev_node.next)
            prev_node.next = node

    def erase(self, index):
        if index < 0:
            raise IndexError("Error: index out of range")
        if index == 0:
            self.pop_front()
        else:
            prev_node = self.__node_before(index)
            prev_node = prev_node.next.next

    def remove_value(self, data):
        if self.__head is None:
            return
        elif self.__head.data == data:
            self.pop_front()
        else:
            node = self.__head
            while node.next is not None and node.next.data == data:
                node = node.next
            if node.next is None:
                return
            else:
                node.next = node.next.next
