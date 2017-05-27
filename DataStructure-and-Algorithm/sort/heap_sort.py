def heap_sort_v1(arr):
    size = len(arr)

    def sift_down(index):
        max_index = index
        while True:
            left_child = 2 * index + 1
            if left_child < size and arr[left_child] > arr[max_index]:
                max_index = left_child
            right_child = 2 * index + 2
            if right_child < size and arr[right_child] > arr[max_index]:
                max_index = right_child

            if max_index == index:
                break
            arr[max_index], arr[index] = arr[index], arr[max_index]
            index = max_index

    # Build Heap: O(N)
    for i in range(size//2, -1, -1):
        sift_down(i)

    # in-place comparsion sort: O(NlogN)
    while size > 1:
        arr[0], arr[size - 1] = arr[size - 1], arr[0]
        size -= 1
        sift_down(0)
    return arr


def heap_sort(arr):
    heap_sort_imp(arr, 0, len(arr) - 1)


def heap_sort_imp(arr, lo, hi):
    size = hi - lo + 1

    def sift_down(index):
        max_index = index
        while True:
            left_child = 2 * index - lo + 1
            if left_child < (lo + size) and arr[left_child] > arr[max_index]:
                max_index = left_child
            right_child = left_child + 1
            if right_child < (lo + size) and arr[right_child] > arr[max_index]:
                max_index = right_child

            if max_index == index:
                break
            arr[max_index], arr[index] = arr[index], arr[max_index]
            index = max_index

    # Build Heap: O(N)
    for i in range(lo + size//2, lo - 1, -1):
        sift_down(i)

    while size > 1:
        arr[lo], arr[lo + size - 1] = arr[lo + size - 1], arr[lo]
        size -= 1
        sift_down(lo)
