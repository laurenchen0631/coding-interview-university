class Hashtable:

    __MIN_CAPACITY = 8
    __GROWTH_FACTOR = 2
    __SHRINK_FACTOR = 4

    __DELETED_FLAG = 0

    def __init__(self):
        self.__capacity = self.__MIN_CAPACITY
        self.__size = 0
        self.__data = [None] * self.__capacity

    def hash(self, key, m):
        if self.__capacity <= m or m <= 0:
            return None
        # h(k, m) = (h1(k) + i*h2(k)) mod m
        h1 = hash(key)
        h2 = (hash(key) << 1) + 1
        return (h1 + m*h2) % self.__capacity

    def __setitem__(self, key, value):
        self.add(key, value)

    def add(self, key, value):
        keyindex = self.__keyindex(key)
        if keyindex:
            self.__data[keyindex].value = value
            return

        self.__adjust_size(self.__size + 1)
        for i in range(1, self.__capacity):
            index = self.hash(key, i)
            if (self.__data[index] is None or
                    self.__data[index] == Hashtable.__DELETED_FLAG):
                self.__data[index] = KeyValuePair(key, value)
                break

    def update(self, key, value):
        keyindex = self.__keyindex(key)
        if keyindex:
            self.__data[keyindex].value = value
        else:
            raise KeyError(str(key))

    def __contains__(self, key):
        return self.exist(key)

    def exist(self, key):
        keyindex = self.__keyindex(key)
        return keyindex is not None

    def __getitem__(self, key):
        return self.get(key)

    def get(self, key):
        keyindex = self.__keyindex(key)
        if keyindex:
            return self.__data[keyindex].value
        raise KeyError(str(key))

    def remove(self, key):
        keyindex = self.__keyindex(key)
        if keyindex:
            self.__data[keyindex] = Hashtable.__DELETED_FLAG
            self.__adjust_size(self.__size - 1)

    def __keyindex(self, key):
        for i in range(1, self.__capacity):
            index = self.hash(key, i)
            if self.__data[index] is None:
                return None
            elif self.__data[index] == Hashtable.__DELETED_FLAG:
                continue
            elif self.__data[index].key == key:
                return index
        return None

    def debugPrint(self):
        for i in range(self.__capacity):
            print(i, "\t", self.__data[i])

    def __adjust_size(self, size):
        if size == self.__capacity:
            self.__increaseCapacity()
        elif (self.__MIN_CAPACITY < self.__capacity and
                size < self.__capacity // self.__SHRINK_FACTOR):
            self.__shrinkCapacity()
        self.__size = size

    def __increaseCapacity(self):
        self.__capacity *= self.__GROWTH_FACTOR
        data = [None] * self.__capacity

        for pair in self.__data:
            if pair is None or pair == self.__DELETED_FLAG:
                continue
            for i in range(1, self.__capacity):
                index = self.hash(pair.key, i)
                if data[index] is None:
                    data[index] = pair
                    break

        self.__data = data

    def __shrinkCapacity(self):
        self.__capacity //= self.__GROWTH_FACTOR
        data = [None] * self.__capacity

        for pair in self.__data:
            if pair is None or pair == Hashtable.__DELETED_FLAG:
                continue
            for i in range(1, self.__capacity):
                index = self.hash(pair.key, i)
                if data[index] is None:
                    data[index] = pair
                    break

        self.__data = data


class KeyValuePair:
    def __init__(self, key, value):
        self.__key = key
        self.value = value

    @property
    def key(self):
        return self.__key

    # def __del__(self):
        # self.__dict.remove(key)
