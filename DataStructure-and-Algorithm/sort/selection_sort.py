def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if i != min:
            arr[i], arr[min] = arr[min], arr[i]
