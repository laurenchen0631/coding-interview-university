from Node import node


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def __str__(self):
        data = []
        node = self.__head
        while node is not None:
            data.append(str(node.data))
            node = node.next
        return "->".join(data)

    # returns number of data elements in list
    def size(self):
        return self.__size

    # bool returns true if empty
    def empty(self):
        return self.__size == 0

    # returns the value of the nth item (starting at 0 for first)
    def value_at(self, index):
        if index < 0 or self.__size <= index:
            raise IndexError("Error: index out of range")
        node = self.__head
        for _ in range(index):
            node = node.next
        return node.data

    # adds an item to the front of the list
    def push_front(self, data):
        node = Node(data, self.__head)
        self.__head = node
        if self.__size == 0:
            self.__tail = node
        self.__size += 1

    # remove front item and return its value
    def pop_front(self):
        if self.__size < 1:
            raise IndexError("Unable to pop from empty list")

        node = self.__head
        self.__head = self.__head.next
        self.__size -= 1

        if self.__size == 0:
            self.__tail = None

        return node.data

    # adds an item at the end
    def push_back(self, data):
        node = Node(data)
        if self.__size == 0:
            self.__head = node
        else:
            self.__tail.next = node
        self.__tail = node
        self.__size += 1

    # removes end item and returns its value
    def pop_back(self):
        if self.__tail is None:
            raise IndexError("Unable to pop from empty list")

        self.__size -= 1
        node = self.__tail
        if self.__size == 0:
            self.__head = None
            self.__tail = None
        else:
            p = self.__head
            while p.next.next is not None:
                p = p.next
            self.__tail = p
            self.__tail.next = None
        return node.data

    # get value of front item
    def front(self):
        return self.__head.data

    # get value of end item
    def back(self):
        return self.__tail.data

    # insert value at index,
    # so current item at that index is pointed to by new item at index
    def insert(self, index, data):
        if index < 0 or self.__size < index:
            raise IndexError("Error: index out of range")

        if index == 0:
            self.push_front(data)
        elif index == self.__size:
            self.push_back(data)
        else:
            prev_node = self.__node_before(index)
            node = Node(data, prev_node.next)
            prev_node.next = node
            self.__size += 1

    # removes node at given index
    def erase(self, index):
        if index < 0 or self.__size <= index:
            raise IndexError("Error: index out of range")

        if index == 0:
            self.pop_front()
        elif index == self.__size - 1:
            self.pop_back()
        else:
            node = self.__node_before(index)
            node.next = node.next.next
            self.__size -= 1

    # returns the value of the node at nth position from the end of the list
    def value_n_from_end(self, n):
        if n < 1 or self.__size < n:
            raise IndexError("Error: index out of range")

        flag_node = self.__head
        for _ in range(n - 1):
            flag_node = flag_node.next
        node = self.__head
        while flag_node is not self.__tail:
            flag_node = flag_node.next
            node = node.next
        return node.data

    # reverses the list
    def reverse(self):
        if self.__head is self.__tail:
            return

        next_node = self.__head.next
        self.__head.next = None
        new_list_head = self.__head
        while next_node is not None:
            node = next_node
            next_node = next_node.next
            node.next = new_list_head
            new_list_head = node

        self.__tail = self.__head
        self.__head = new_list_head

    def remove_value(self, data):
        if self.__head is None:
            return
        node = self.__head
        if node.data == data:
            self.pop_front()
        while node.next is not None:
            if node.next.data == data:
                break
            node = node.next

        if node.next is None:
            return
        node.next = node.next.next
        if node.next is None:
            self.__tail = node

        self.__size -= 1

    def __node_before(self, index):
        if index == 0:
            return None

        p = self.__head
        for i in range(index - 1):
            p = p.next
        return p
