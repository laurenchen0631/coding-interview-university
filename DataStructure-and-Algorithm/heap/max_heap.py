class MaxHeap:

    def __init__(self):
        self.__data = []
        self.__size = 0

    def __len__(self):
        return self.get_size()

    def __str__(self):
        return str(self.__data)

    def insert(self, value):
        self.__data.append(value)
        self.__size += 1
        self.__sift_up(self.__data, len(self) - 1)

    def __sift_up(self, arr, index):
        parent = self.__parent(index)
        while index > 0 and arr[parent] < arr[index]:
            arr[parent], arr[index] = arr[index], arr[parent]
            index = parent
            parent = self.__parent(index)

    def __parent(self, index):
        return (index - 1) // 2

    def __sift_down(self, arr, index):
        max_index = index

        while True:
            # check left and right chlid to determine which is greater
            left_child = self.__left_child(index)
            if left_child < len(self) and arr[left_child] > arr[max_index]:
                max_index = left_child

            right_child = self.__right_child(index)
            if (right_child < len(self) and
                    arr[right_child] > arr[max_index]):
                max_index = right_child

            if index != max_index:
                arr[max_index], arr[index] = arr[index], arr[max_index]
                index = max_index
            else:
                break

    def __left_child(self, index):
        return 2 * index + 1

    def __right_child(self, index):
        return 2 * index + 2

    def get_size(self):
        return self.__size

    def is_empty(self):
        return self.get_size() == 0

    def get_max(self):
        return self.__data[0] if self.__data else None

    def extract_max(self):
        if not self.__data:
            return None
        elif len(self) == 1:
            self.__size = 0
            return self.__data.pop()

        max = self.__data[0]
        self.__size -= 1
        self.__data[0] = self.__data.pop()
        self.__sift_down(self.__data, 0)
        return max

    def remove(self, index):
        if not (0 <= index < len(self)):
            raise IndexError

        self.__data[index] = self.__data[0] + 1
        self.__sift_up(self.__data, index)
        self.extract_max()

    def replace(self, index, value):
        old_value = self.__data[index]
        self.__data[index] = value
        if value > old_value:
            self.__sift_up(self.__data, index)
        else:
            self.__sift_down(self.__data, index)

    # create a heap from an array of elements, needed for heap_sort
    @classmethod
    def heapify(cls, arr, copy=True):
        heap = cls()
        heap.__size = len(arr)
        if copy:
            heap.__data = arr[:]
            arr = heap.__data

        for i in range(len(arr)//2, -1, -1):
            heap.__sift_down(arr, i)
        return heap

    # take an unsorted array and
    # turn it into a sorted array in-place using a max heap
    @classmethod
    def heap_sort(cls, arr):
        heap = cls.heapify(arr, False)
        for _ in range(len(arr)):
            arr[0], arr[heap.__size-1] = arr[heap.__size-1], arr[0]
            heap.__size -= 1
            heap.__sift_down(arr, 0)
