class ArrayQueue:
    def __init__(self):
        self.__SIZE = 15 + 1  # one position is preserved to prevent from full
        self.__collection = [None] * self.__SIZE
        self.__read_index = 0
        self.__write_index = 0

    def enqueue(self, value):
        if self.full():
            raise BufferError("Error: Can't enqueue a full queue.")

        self.__collection[self.__write_index] = value
        self.__write_index += 1
        if self.__write_index == self.__SIZE:
            self.__write_index = 0

    def dequeue(self):
        if self.empty():
            raise BufferError("Error: Can't dequeue an empty queue.")

        data = self.__collection[self.__read_index]
        self.__read_index += 1
        if self.__read_index == self.__SIZE:
            self.__read_index = 0

        return data

    def full(self):
        return (
            self.__write_index - self.__read_index == self.__SIZE - 1 or
            self.__write_index == self.__read_index - 1)

    def empty(self):
        return self.__write_index == self.__read_index


class LinkedListQueue:
    def __init__(self):
        self.__collection = DoublyLinkList()

    def enqueue(self, value):
        self.__collection.push_front(value)

    def dequeue(self):
        return self.__collection.pop_back()

    def empty(self):
        return self.__collection.empty()


class DoublyLinkList:
    def __init__(self):
        sentinel = ListNode()
        sentinel.next = sentinel.prev = sentinel
        self.__head = sentinel
        self.__size = 0

    def push_front(self, data):
        node = ListNode(data, self.__head.next, self.__head)
        self.__head.next.prev = node
        self.__head.next = node
        self.__size += 1

    def pop_back(self):
        if self.__head.prev == self.__head:
            raise IndexError("Can't pop an empty list")
        node = self.__head.prev
        node.prev.next = self.__head
        self.__head.prev = node.prev
        self.__size -= 1

        return node.data

    def empty(self):
        return self.__size == 0


class ListNode:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.prev = prev
        self.next = next
